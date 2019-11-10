from DMP.District.Models.State import *
from DMP.District.Models.Country import *
from django.core.exceptions import ObjectDoesNotExist


class StateService:
    errors = None

    def __init__(self):
        pass

    def list(self, country_id):
        country = Country.objects.get(id=country_id)
        serializer = StateSerializer(country.states.all(), many=True)
        # serializer = StateSerializer(State.objects.filter(country=country_id), many=True)
        return serializer.data

    def detail(self, country_id, id):
        try:
            state = State.objects.get(pk=id, country_id=country_id)
        except ObjectDoesNotExist:
            return {}
        serializer = StateSerializer(state)
        return serializer.data
