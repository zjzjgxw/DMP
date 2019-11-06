from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from DMP.Helps.func import return_format
from DMP.District.models import *

class DistrictViewSet(ViewSet):
    """
    业务日志类
    """

    def list(self, request):
        country = Country.objects.first()
        return Response(return_format(200, "hello"))

    def create(self, request):
        return Response(return_format(20001, "msg"))

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
