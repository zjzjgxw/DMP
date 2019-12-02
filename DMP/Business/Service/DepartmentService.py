from DMP.Core.Service import BasicService
from DMP.Core.Exceptions import ValidationException
from DMP.Business.Models.Department import DepartmentSerializer


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
