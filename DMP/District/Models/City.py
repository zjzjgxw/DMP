from .Place import *
from rest_framework.serializers import ModelSerializer


class City(Place):
    country = models.ForeignKey('Country', db_constraint=False, related_name='city_country',
                                on_delete=models.SET_DEFAULT,
                                default=0)
    state = models.ForeignKey('State', db_constraint=False, related_name='cities', on_delete=models.SET_DEFAULT,
                              default=0)


class CitySerializer(ModelSerializer):
    """城市序列化"""

    class Meta:
        model = City
        fields = ['id', 'name', 'name_en', 'country_id', 'state_id']
