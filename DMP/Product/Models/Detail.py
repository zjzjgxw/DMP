from django.db import models
from rest_framework import serializers
from DMP.Core.Paginate import PageManager
from django.db import transaction, IntegrityError
from DMP.Product.Models.Category import Category
from DMP.Core.Exceptions import ValidationException


class DetailManager(PageManager):
    pass


class Detail(models.Model):
    """
    商品详情
    """
    STOCK_TYPE_BUY = 1
    STOCK_TYPE_PAID = 2
    STOCK_TYPE_CHOICES = (
        (STOCK_TYPE_BUY, '拍下减库存'),
        (STOCK_TYPE_PAID, '付款减库存')
    )

    business_id = models.PositiveIntegerField("商户id")
    name = models.CharField("商品名称", max_length=255, default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='category_id',
                                 db_constraint=False)
    model = models.PositiveSmallIntegerField("交易模式", default=1)
    stock_type = models.PositiveSmallIntegerField("库存方式", choices=STOCK_TYPE_CHOICES, default=STOCK_TYPE_BUY)
    delete_flag = models.PositiveSmallIntegerField("删除标记", default=0)
    created_at = models.DateTimeField("产生时间", auto_now_add=True)
    updated_at = models.DateTimeField("修改时间", auto_now=True)
    objects = DetailManager()


class DetailAttribute(models.Model):
    """
    商品属性
    """
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE, db_column='detail_id',
                               db_constraint=False)
    name = models.CharField("属性名称", max_length=10, default="")
    option = models.CharField("属性值", max_length=10, default="")
    created_at = models.DateTimeField("产生时间", auto_now_add=True)

    class Meta:
        db_table = 'product_detail_attribute'


class DescribeImages(models.Model):
    """
    商品描述图片
    """
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE, db_column='detail_id',
                               db_constraint=False)
    img_id = models.BigIntegerField("图片文件id")
    index_no = models.PositiveIntegerField("图片次序", default=0)

    class Meta:
        db_table = 'product_detail_desc_img'


class MainImages(models.Model):
    """
    商品主图片
    """
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE, db_column='detail_id',
                               db_constraint=False)
    img_id = models.BigIntegerField("图片文件id")
    index_no = models.PositiveIntegerField("图片次序", default=0)

    class Meta:
        db_table = 'product_detail_main_img'


class Snapshot(models.Model):
    """
    商品快照
    """
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE, db_column='detail_id',
                               db_constraint=False)
    json_content = models.TextField("快照信息", default="")
    created_at = models.DateTimeField("产生时间", auto_now_add=True)

    class Meta:
        db_table = 'product_detail_snapshot'


class DetailAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailAttribute
        fields = ["id", "detail", "name", "option"]


class DescribeImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescribeImages
        fields = ["id", "detail", "img_id", "index_no"]


class MainImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainImages
        fields = ["id", "detail", "img_id", "index_no"]


class DetailSerializer(serializers.ModelSerializer):
    main_images = serializers.ListField()
    describe_images = serializers.ListField()
    attribute_list = serializers.ListField()

    def get_main_images(self, obj):
        pass

    def get_describe_images(self, obj):
        pass

    def get_attribute_list(self, obj):
        pass

    def validate_attribute_list(self, attrs):
        for item in attrs:
            if not isinstance(item, dict):
                raise ValidationException(20016)
            if "name" not in item or "option" not in item:
                raise ValidationException(20016)
            if not isinstance(item["name"], str):
                raise ValidationException(20016)
            if not isinstance(item["option"], str):
                raise ValidationException(20016)

    def create(self, validated_data):
        try:
            with transaction.atomic('ProductMysql'):
                detail_data = validated_data
                del detail_data["attribute_list"]
                del detail_data["describe_images"]
                del detail_data["main_images"]
                detail = Detail(**detail_data)
                detail.save()
                attribute_list = []
                for item in validated_data['attribute_list']:
                    attribute_list.append(DetailAttribute(detail_id=detail.id, **item))
                DetailAttribute.objects.bulk_create(attribute_list)
                main_image_list = []
                for item in validated_data['main_images']:
                    main_image_list.append(MainImages(detail_id=detail.id, **item))
                MainImages.objects.bulk_create(main_image_list)
                describe_image_list = []
                for item in validated_data["describe_images"]:
                    describe_image_list.append(DescribeImages(detail_id=detail.id, **item))
                DescribeImages.objects.bulk_create(describe_image_list)
                return detail
        except IntegrityError:
            raise
        except:
            raise

    class Meta:
        model = Detail
        fields = ["id", "business_id", "category", "name", "model", "stock_type", "attribute_list", "main_images",
                  "describe_images"]
        extra_kwargs = {'name': {'required': True}, 'business_id': {'required': True}}


class SnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snapshot
        fields = ["id", "detail", "json_content", "created_at", "stock_type"]
        extra_kwargs = {'json_content': {'required': True}}
