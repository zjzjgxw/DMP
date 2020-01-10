from django.db import models
from rest_framework import serializers
from DMP.Core.Paginate import PageManager
from DMP.Product.Models.Category import Category


class DetailManager(PageManager):
    def detail(self, pk, business_id):
        return self.get(id=pk, business_id=business_id, delete_flag=0)


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
    class Meta:
        model = Detail
        fields = ["id", "business_id", "category", "name", "model", "stock_type"]
        extra_kwargs = {'name': {'required': True}, 'business_id': {'required': True}, 'stock_type': {'required': True}}


class SnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snapshot
        fields = ["id", "detail", "json_content", "created_at"]
        extra_kwargs = {'json_content': {'required': True}}
