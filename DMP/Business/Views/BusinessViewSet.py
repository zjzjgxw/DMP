from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from DMP.Business.Service.BusinessService import BusinessService
from DMP.Helps.func import return_format
from rest_framework.decorators import action
from DMP.Core.Token import auth_permission_required


class BusinessViewSet(ViewSet):
    """
    商户视图
    """

    def list(self, request):
        pass

    def create(self, request):
        business_id = BusinessService.create(**request.data)
        return Response(return_format(200, data={"id": business_id}))

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

    @action(methods=["get"], detail=False)
    @auth_permission_required(["business_permission_list"])
    def permissions(self, request):
        business_id = request.dmp_user['business_id']
        data = BusinessService.permissions(business_id=business_id)
        return Response(return_format(200, data=data))

    @action(methods=["get"], detail=False)
    @auth_permission_required(["business_group_list"])
    def groups(self, request):
        data = BusinessService.groups()
        return Response(return_format(200, data=data))
