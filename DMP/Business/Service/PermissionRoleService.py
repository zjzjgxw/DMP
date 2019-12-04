from DMP.Core.Service import BasicService
from DMP.Core.Exceptions import ValidationException, ObjectDoesNotExistException
from DMP.Business.Models.PermissionRole import PermissionRoleSerializer, PermissionRole
from django.core.exceptions import ObjectDoesNotExist


class PermissionRoleService(BasicService):
    """
    部门服务
    """

    @classmethod
    def create(cls, **kwargs):
        """
        创建部门
        :param kwargs:
        :return:
        """
        serializer = PermissionRoleSerializer(data=kwargs)
        if serializer.is_valid():
            role = serializer.save()
            return role.id
        else:
            raise ValidationException(detail=serializer.errors)
