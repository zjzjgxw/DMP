from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from DMP.Business.Service.PermissionRoleService import PermissionRoleService
from DMP.Helps.func import return_format
from DMP.Core.Token import auth_permission_required
from DMP.Core.Exceptions import ValidationException


class PermissionRoleViewSet(ViewSet):
    """
    职位视图
    """

    def list(self, request):
        pass

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

    def destroy(self, request, pk=None):
        pass
