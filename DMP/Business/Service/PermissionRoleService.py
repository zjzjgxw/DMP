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

    @classmethod
    def update(cls, name, role_desc, permission_role_id, business_id):
        try:
            permission_role = PermissionRole.objects.detail(permission_role_id=permission_role_id,
                                                            business_id=business_id)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExistException()
        data = {"name": name}
        if role_desc is not None:
            data["role_desc"] = role_desc
        serializer = PermissionRoleSerializer(instance=permission_role, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
        else:
            raise ValidationException(detail=serializer.errors)
