from DMP.Core.Service import BasicService
from DMP.Core.Exceptions import ValidationException, ObjectDoesNotExistException
from DMP.Business.Models.PermissionRole import PermissionRoleSerializer, PermissionRole, PermissionRoleRelation
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.db import IntegrityError


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

    @classmethod
    def delete(cls, permission_role_id, business_id):
        try:
            permission_role = PermissionRole.objects.detail(permission_role_id=permission_role_id,
                                                            business_id=business_id)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExistException()
        serializer = PermissionRoleSerializer(instance=permission_role, data={"delete_flag": 1}, partial=True)
        if serializer.is_valid():
            serializer.save()
        else:
            raise ValidationException(detail=serializer.errors)

    @classmethod
    def list(cls, business_id, page=1, page_size=10):
        count = PermissionRole.objects.count(business_id)
        role_list = PermissionRole.objects.list(business_id, page, page_size)
        serializer = PermissionRoleSerializer(role_list, many=True)
        return {"list": serializer.data, "count": count}

    @classmethod
    def permissions(cls, permission_role_id, business_id):
        try:
            permission_role = PermissionRole.objects.detail(permission_role_id=permission_role_id,
                                                            business_id=business_id)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExistException()
        relations = PermissionRoleRelation.objects.filter(role=permission_role)
        data = []
        for relation in relations:
            data.append(relation.permission_id)
        return data

    @classmethod
    def add_permissions(cls, permission_role_id, business_id, permission_ids):
        try:
            PermissionRole.objects.detail(permission_role_id=permission_role_id,
                                          business_id=business_id)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExistException()
        try:
            with transaction.atomic('BusinessMysql'):
                PermissionRoleRelation.objects.filter(role=permission_role_id).delete()
                query_set_list = []
                for permission_id in permission_ids:
                    query_set_list.append(
                        PermissionRoleRelation(role_id=permission_role_id, permission_id=permission_id))
                PermissionRoleRelation.objects.bulk_create(query_set_list)
                return True
        except IntegrityError:
            raise
