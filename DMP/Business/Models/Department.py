from django.db import models
from DMP.Business.Models.BasicInfo import BasicInfo
from DMP.Business.Models.User import User


class Department(models.Model):
    """
    部门结构
    """
    business = models.ForeignKey(BasicInfo, on_delete=models.SET_NULL, db_column='business_basic_id',
                                 db_constraint=False)
    name = models.CharField("部门名称", max_length=100, default="")
    parent_id = models.PositiveIntegerField("父节点id", default=0)
    delete_flag = models.PositiveSmallIntegerField("删除标记", default=0)
    created_at = models.DateTimeField("产生时间", auto_now_add=True)
    updated_at = models.DateTimeField("修改时间", auto_now=True)
    usrs = models.ManyToManyField(User, through='DepartmentUserRelation', through_fields=('department', 'user'))


class DepartmentUserRelation(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, db_constraint=False,
                                   db_column='business_department_id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_constraint=False, db_column='business_user_id')

    class Meta:
        db_table = 'business_user_department_relation'
