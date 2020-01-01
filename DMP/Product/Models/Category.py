from django.db import models
from rest_framework.serializers import ModelSerializer


class Category(models.Model):
    """
    商品类目
    """
    business_id = models.PositiveIntegerField("商户id")
    name = models.CharField("类目名称", max_length=10, default="")
    parent_id = models.PositiveIntegerField("父节点id", default=0)
    delete_flag = models.PositiveSmallIntegerField("删除标记", default=0)
    created_at = models.DateTimeField("产生时间", auto_now_add=True)
    updated_at = models.DateTimeField("修改时间", auto_now=True)


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'business_id', 'name', 'parent_id']
        extra_kwargs = {'name': {'required': True}, 'business_id': {'required': True}}


class CategoryAttribute(models.Model):
    """
    类目属性
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='category_id',
                                 db_constraint=False)
    name = models.CharField("属性名称", max_length=10, default="")
    option = models.CharField("属性值", max_length=10, default="")
    created_at = models.DateTimeField("产生时间", auto_now_add=True)
    updated_at = models.DateTimeField("修改时间", auto_now=True)

    class Meta:
        db_table = 'product_category_attribute'


class CategorySpecification(models.Model):
    """
    类目规格
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='category_id',
                                 db_constraint=False)
    name = models.CharField("规格名称", max_length=10, default="")
    option = models.CharField("规格值", max_length=10, default="")
    created_at = models.DateTimeField("产生时间", auto_now_add=True)
    updated_at = models.DateTimeField("修改时间", auto_now=True)

    class Meta:
        db_table = 'product_category_specification'
