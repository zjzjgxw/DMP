from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from DMP.Business.Service.BusinessService import BusinessService
from DMP.Helps.func import return_format


class BusinessAuthInfoViewSet(ViewSet):
    """
    商户认证视图
    """

    def list(self, request):
        pass

    def create(self, request):
        res = BusinessService.auth(**request.data)
        return Response(return_format(200, data=res))

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
