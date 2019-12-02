from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from DMP.Helps.func import return_format
from DMP.Core.Token import auth_permission_required
from DMP.Business.Service.DepartmentService import DepartmentService
from DMP.Core.Exceptions import ValidationException


class DepartmentViewSet(ViewSet):
    """
    部门视图
    """

    @auth_permission_required(["department_list"])
    def list(self, request):
        return Response(return_format(200))

    @auth_permission_required(["department_create"])
    def create(self, request):
        business_id = request.dmp_user['business_id']
        if "list" not in request.data:
            raise ValidationException()
        params = request.data['list']
        for item in params:
            item['business'] = business_id
        DepartmentService.create(params)
        return Response(return_format(200, msg="创建成功"))

        def retrieve(self, request, pk=None):
            pass

        def update(self, request, pk=None):
            pass

        def partial_update(self, request, pk=None):
            pass

        def destroy(self, request, pk=None):
            pass
