from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from DMP.Helps.func import return_format
from DMP.District.Services.StateService import StateService


class StateView(ViewSet):
    """
    省份View
    """

    def list(self, request, country_id=None):
        service = StateService()
        return Response(return_format(200, data=service.list(country_id=country_id)))

    def create(self, request):
        pass

    def retrieve(self, request, country_id=None, pk=None):
        service = StateService()
        return Response(return_format(200, data=service.detail(id=pk, country_id=country_id)))

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
