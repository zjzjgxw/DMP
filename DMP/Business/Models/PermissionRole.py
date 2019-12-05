from django.db import models
from DMP.Business.Models.BasicInfo import BasicInfo
from DMP.Business.Models.Permission import Permission
from rest_framework import serializers


class PermissionRoleManager(models.Manager):
    def detail(self, permission_role_id, business_id):
        return self.get(id=permission_role_id, business=business_id, delete_flag=0)


class PermissionRole(models.Model):
    """
    权限角色
    """
    business = models.ForeignKey(BasicInfo, on_delete=models.CASCADE, db_column='business_basic_id',
                                 db_constraint=False)
    name = models.CharField("角色名称", max_length=20, default="")
    role_desc = models.CharField("描述", max_length=200, default="")
    delete_flag = models.PositiveSmallIntegerField("删除标记", default=0)
    created_at = models.DateTimeField("产生时间", auto_now_add=True)
    updated_at = models.DateTimeField("修改时间", auto_now=True)
    permissions = models.ManyToManyField(Permission, through='PermissionRoleRelation',
                                         through_fields=("role", "permission"))
    objects = PermissionRoleManager()

    class Meta:
        db_table = 'business_permission_role'


class PermissionRoleRelation(models.Model):
    role = models.ForeignKey(PermissionRole, on_delete=models.CASCADE, db_constraint=False,
                             db_column='business_permission_role_id')
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE, db_constraint=False,
                                   db_column='business_permission_id')

    class Meta:
        db_table = 'business_permission_role_relation'


class PermissionRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermissionRole
        fields = ['id', 'name', 'role_desc', 'business']
        extra_kwargs = {'role_desc': {'required': False}, 'name': {'required': True}}
