from django.db import models
from rest_framework import serializers


class PermissionGroup(models.Model):
    """
    权限组
    """
    name = models.CharField("权限名称", max_length=20, default="")
    permission_desc = models.CharField("描述", max_length=200, default="")
    delete_flag = models.PositiveSmallIntegerField("删除标记", default=0)
    created_at = models.DateTimeField("产生时间", auto_now_add=True)
    updated_at = models.DateTimeField("修改时间", auto_now=True)

    class Meta:
        db_table = 'business_permission_group'


class PermissionGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermissionGroup
        fields = ['id', 'name', 'permission_desc']
        extra_kwargs = {'permission_desc': {'required': False}, 'name': {'required': True}}
