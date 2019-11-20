from django.db import models
from DMP.Business.Models.PermissionGroup import PermissionGroup


class Permission(models.Model):
    """
    权限
    """
    group = models.ForeignKey(PermissionGroup, on_delete=models.SET_NULL, db_column='business_permission_group_id',
                              db_constraint=False)
    name = models.CharField("权限名称", max_length=20, default="")
    permission_desc = models.CharField("权限描述", max_length=200, default="")
    delete_flag = models.PositiveSmallIntegerField("删除标记", default=0)
    created_at = models.DateTimeField("产生时间", auto_now_add=True)
    updated_at = models.DateTimeField("修改时间", auto_now=True)
