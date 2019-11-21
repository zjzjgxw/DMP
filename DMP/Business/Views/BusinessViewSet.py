from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from DMP.Business.Service.BusinessService import BusinessService
from DMP.Helps.func import return_format


class BusinessViewSet(ViewSet):
    """
    商户视图
    """

    def list(self, request):
        pass

    def create(self, request):
        res = BusinessService.create(**request.data)
        if res:
            return Response(return_format(200, data=res))
        else:
            return Response(return_format(BusinessService.error_code,data=BusinessService.errors))

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
