from django.db import models
from DMP.Business.Models.BasicInfo import BasicInfo
from DMP.Business.Models.User import User
from rest_framework import serializers


class DepartmentManager(models.Manager):
    def detail(self, department_id, business_id):
        return self.get(id=department_id, business=business_id, delete_flag=0)

    def tree(self, business_id):
        """
        获取某个商户的部门树形结构
        :param business_id:
        :return:
        """
        department_list = list(self.filter(business=business_id, delete_flag=0))
        department_dict = {}
        for department in department_list:
            department_dict[department.id] = department
        root_list = []
        for department in department_list:
            if department.parent_id == 0:
                root_list.append(department)
            else:
                department_dict[department.parent_id].add_child(department)
        return DepartmentSerializer(root_list, many=True).data


class Department(models.Model):
    """
    部门结构
    """
    business = models.ForeignKey(BasicInfo, on_delete=models.CASCADE, db_column='business_basic_id',
                                 db_constraint=False)
    name = models.CharField("部门名称", max_length=100, default="")
    parent_id = models.PositiveIntegerField("父节点id", default=0)
    delete_flag = models.PositiveSmallIntegerField("删除标记", default=0)
    created_at = models.DateTimeField("产生时间", auto_now_add=True)
    updated_at = models.DateTimeField("修改时间", auto_now=True)
    user = models.ManyToManyField(User, through='DepartmentUserRelation', through_fields=('department', 'user'))
    children = None
    objects = DepartmentManager()

    def add_child(self, obj):
        if self.children is None:
            self.children = [obj]
        else:
            self.children.append(obj)


class DepartmentUserRelation(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, db_constraint=False,
                                   db_column='business_department_id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_constraint=False, db_column='business_user_id')

    class Meta:
        db_table = 'business_user_department_relation'


class DepartmentSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    def get_children(self, obj):
        """
        自定义获取children数据
        :param obj:
        :return:
        """
        if obj.children is None:
            return []
        else:
            return DepartmentSerializer(obj.children, many=True).data

    class Meta:
        model = Department
        fields = ['id', 'name', 'parent_id', 'business', 'children']
        extra_kwargs = {'name': {'required': True}}
