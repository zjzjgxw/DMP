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
        business_id = request.dmp_user['business_id']
        res = DepartmentService.list(business_id)
        return Response(return_format(200, data=res))

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

    @auth_permission_required(["department_update"])
    def update(self, request, pk=None):
        business_id = request.dmp_user['business_id']
        if "name" not in request.data:
            raise ValidationException()
        name = request.data['name']
        DepartmentService.update(name=name, department_id=pk, business_id=business_id)
        return Response(return_format(200, msg="修改成功"))

    def partial_update(self, request, pk=None):
        pass

    @auth_permission_required(["department_delete"])
    def destroy(self, request, pk=None):
        business_id = request.dmp_user['business_id']
        DepartmentService.delete(department_id=pk, business_id=business_id)
        return Response(return_format(200, msg="删除成功"))
