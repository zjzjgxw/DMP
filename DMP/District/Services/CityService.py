from DMP.District.Models.State import *
from DMP.District.Models.City import *
from django.core.exceptions import ObjectDoesNotExist


class CityService:
    errors = None

    def __init__(self):
        pass

    def list(self, state_id, country_id=None):
        """
        省份下所有城市列表
        :param state_id:
        :param country_id:
        :return:
        """
        state = State.objects.get(id=state_id)
        serializer = CitySerializer(state.cities.all(), many=True)
        return serializer.data

    def detail(self, state_id, city_id):
        try:
            city = City.objects.get(pk=city_id, state_id=state_id)
        except ObjectDoesNotExist:
            return {}
        serializer = CitySerializer(city)
        return serializer.data
