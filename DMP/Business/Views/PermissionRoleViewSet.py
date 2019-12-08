from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from DMP.Business.Service.PermissionRoleService import PermissionRoleService
from DMP.Helps.func import return_format
from DMP.Core.Token import auth_permission_required
from DMP.Core.Exceptions import ValidationException
from rest_framework.decorators import action
from DMP.Core.Paginate import PagePaginate


class PermissionRoleViewSet(ViewSet):
    """
    职位视图
    """

    @auth_permission_required(["permission_role_list"])
    def list(self, request):
        business_id = request.dmp_user['business_id']
        page_paginate = PagePaginate(request)
        data = PermissionRoleService.list(business_id, page_paginate.page, page_paginate.page_size)
        return Response(return_format(200, data=data))

    @auth_permission_required(["permission_role_create"])
    def create(self, request):
        business_id = request.dmp_user['business_id']
        role_id = PermissionRoleService.create(**request.data, business=business_id)
        return Response(return_format(200, data={"id": role_id}))

    def retrieve(self, request, pk=None):
        pass

    @auth_permission_required(["permission_role_update"])
    def update(self, request, pk=None):
        business_id = request.dmp_user['business_id']
        if "name" not in request.data:
            raise ValidationException()
        if "role_desc" in request.data:
            role_desc = request.data['role_desc']
        else:
            role_desc = None
        name = request.data['name']
        PermissionRoleService.update(name=name, role_desc=role_desc, permission_role_id=pk, business_id=business_id)
        return Response(return_format(200, msg="修改成功"))

    def partial_update(self, request, pk=None):
        pass

    @auth_permission_required(["permission_role_delete"])
    def destroy(self, request, pk=None):
        business_id = request.dmp_user['business_id']
        PermissionRoleService.delete(permission_role_id=pk, business_id=business_id)
        return Response(return_format(200, msg="删除成功"))

    @action(methods=["get", "post"], detail=True)
    @auth_permission_required(["permission_role_permissions"])
    def permissions(self, request, pk=None):
        """
        修改职位所拥有的权限
        :param request:
        :param pk:
        :return:
        """
        business_id = request.dmp_user['business_id']
        if request.method == "POST":
            if "permission_ids" not in request.data:
                raise ValidationException()
            permission_ids = request.data['permission_ids']
            if type(permission_ids) != list:
                raise ValidationException(10007)
            PermissionRoleService.add_permissions(permission_role_id=pk, business_id=business_id,
                                                  permission_ids=permission_ids)
            return Response(return_format(200))
        elif request.method == "GET":
            data = PermissionRoleService.permissions(permission_role_id=pk, business_id=business_id)
            return Response(return_format(200, data=data))
