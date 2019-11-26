from django.db import models
from DMP.Business.Models.Permission import Permission
from rest_framework.serializers import ModelSerializer


class BasicInfo(models.Model):
    """
    商户基础信息表
    """
    name = models.CharField("商户名称", max_length=30, default="")
    logo_img_id = models.BigIntegerField("头像文件id", default=0)
    email = models.EmailField("账号名", max_length=100, default="", unique=True)
    delete_flag = models.PositiveSmallIntegerField("删除标记", default=0)
    created_at = models.DateTimeField("产生时间", auto_now_add=True)
    updated_at = models.DateTimeField("修改时间", auto_now=True)
    permissions = models.ManyToManyField(Permission, through='BusinessPermissions',
                                         through_fields=('business', 'permission'),
                                         )


class BusinessPermissions(models.Model):
    business = models.ForeignKey(BasicInfo, on_delete=models.CASCADE, db_constraint=False,
                                 db_column='business_basic_id')
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE, db_constraint=False,
                                   db_column='business_permission_id')

    class Meta:
        db_table = 'business_permission_package'


class BusinessSerializer(ModelSerializer):
    class Meta:
        model = BasicInfo
        fields = ['id', 'name', 'logo_img_id', 'email']
        extra_kwargs = {'email': {'required': True}}
