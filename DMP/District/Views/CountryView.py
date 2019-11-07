from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from DMP.Helps.func import return_format
from DMP.District.Services.CountryService import *


class CountryView(ViewSet):
    """
    国家View
    """

    def list(self, request):
        service = CountryService()
        return Response(return_format(200, data=service.list()))

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        service = CountryService()
        return Response(return_format(200, data=service.detail(pk)))

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
