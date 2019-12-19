from django.db import models
from rest_framework import serializers
from DMP.Business.Models.BasicInfo import BasicInfo
from DMP.Core.Paginate import PageManager


class VendorManager(PageManager):
    pass


class Vendor(models.Model):
    """
    供应商
    """
    business = models.ForeignKey(BasicInfo, on_delete=models.CASCADE, db_column='business_basic_id',
                                 db_constraint=False)
    name = models.CharField("供应商名称", max_length=30, default="")
    unique_code = models.CharField("企业统一编码", max_length=30, default="")
    img_id = models.BigIntegerField("企业营业执照文件id", default=0)
    linkman = models.CharField("联系人姓名", max_length=50, default="")
    linkman_tel = models.CharField("联系人电话", max_length=30, default="")
    email = models.EmailField("邮箱地址", max_length=250, default="")
    country_id = models.PositiveIntegerField("国家id", default=0)
    state_id = models.PositiveIntegerField("省份id", default=0)
    city_id = models.PositiveIntegerField("城市id", default=0)
    address = models.CharField("详细地址", max_length=200, default="")
    delete_flag = models.PositiveSmallIntegerField("删除标记", default=0)
    created_at = models.DateTimeField("产生时间", auto_now_add=True)
    updated_at = models.DateTimeField("修改时间", auto_now=True)

    objects = VendorManager()


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'name', 'unique_code', "business", "img_id", "linkman", "linkman_tel", "email", "country_id",
                  "state_id", "city_id", "address"]
        extra_kwargs = {'name': {'required': True}, 'unique_code': {'required': True}, 'img_id': {'required': True},
                        'linkman': {'required': True},
                        'linkman_tel': {'required': True}, 'email': {'required': True}, "business": {'read_only': True}}
