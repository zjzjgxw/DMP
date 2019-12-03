from DMP.Core.Service import BasicService
from DMP.Core.Exceptions import ValidationException, ObjectDoesNotExistException
from DMP.Business.Models.Department import DepartmentSerializer, Department
from django.core.exceptions import ObjectDoesNotExist


class DepartmentService(BasicService):
    """
    部门服务
    """

    @classmethod
    def create(cls, department_list):
        """
        创建部门
        :param department_list:
        :return:
        """
        serializer = DepartmentSerializer(data=department_list, many=True)
        if serializer.is_valid():
            serializer.save()
            return True
        else:
            raise ValidationException(detail=serializer.errors)

    @classmethod
    def update(cls, name, department_id, business_id):
        try:
            department = Department.objects.detail(department_id=department_id, business_id=business_id)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExistException()
        serializer = DepartmentSerializer(instance=department, data={"name": name}, partial=True)
        if serializer.is_valid():
            serializer.save()
        else:
            raise ValidationException(detail=serializer.errors)

    @classmethod
    def delete(cls, department_id, business_id):
        try:
            department = Department.objects.detail(department_id=department_id, business_id=business_id)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExistException()
        serializer = DepartmentSerializer(instance=department, data={"delete_flag": 1}, partial=True)
        if serializer.is_valid():
            serializer.save()
        else:
            raise ValidationException(detail=serializer.errors)

    @classmethod
    def list(cls, business_id):
        department_list = Department.objects.tree(business_id=business_id)
        return None
