from django.db import models
from rest_framework import serializers


class StockInfo(models.Model):
    """
    库存详情
    """
    product_id = models.PositiveIntegerField("商品id", unique=True)
    currency_code = models.CharField("货币代码", max_length=3, default="CNY")
    default_specifications = models.TextField("json规格详情", blank=True)
    price = models.DecimalField("售价", default=0, max_digits=12, decimal_places=2)
    last_num = models.PositiveIntegerField("剩余库存", default=0)
    sale_num = models.PositiveIntegerField("总销量", default=0)
    created_at = models.DateTimeField("产生时间", auto_now_add=True)
    updated_at = models.DateTimeField("修改时间", auto_now=True)

    class Meta:
        db_table = 'stock_info'


class StockSpecificationDetail(models.Model):
    """
    库存规格详情
    """
    stock = models.ForeignKey(StockInfo, on_delete=models.CASCADE, db_column='stock_info_id',
                              db_constraint=False)
    first_specification_name = models.CharField("属性名称", max_length=10, default="")
    first_specification_value = models.CharField("属性值", max_length=10, default="")
    second_specification_name = models.CharField("属性名称", max_length=10, default="")
    second_specification_value = models.CharField("属性名称", max_length=10, default="")
    price = models.DecimalField("售价", default=0, max_digits=12, decimal_places=2)
    last_num = models.PositiveIntegerField("剩余库存", default=0)
    sku = models.CharField("商品sku", max_length=255, default="")
    created_at = models.DateTimeField("产生时间", auto_now_add=True)
    updated_at = models.DateTimeField("修改时间", auto_now=True)

    class Meta:
        db_table = 'stock_specification_detail'


class StockInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockInfo
        fields = ["id", "product_id", "currency_code", "default_specifications", "price", "last_num", "sale_num"]
        extra_kwargs = {'currency_code': {'required': True}, 'product_id': {'required': True}}
