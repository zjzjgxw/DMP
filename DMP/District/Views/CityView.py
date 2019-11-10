from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from DMP.Helps.func import return_format
from DMP.District.Services.CityService import CityService


class CityView(ViewSet):
    """
    城市View
    """

    def list(self, request, country_id=None, state_id=None):
        service = CityService()
        return Response(return_format(200, data=service.list(state_id=state_id)))

    def create(self, request):
        pass

    def retrieve(self, request, country_id=None, state_id=None, pk=None):
        service = CityService()
        return Response(return_format(200, data=service.detail(state_id, pk)))

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
