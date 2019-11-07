from .Place import *
from rest_framework.serializers import ModelSerializer


class Country(Place):
    class Meta:
        db_table = 'district_country'


class CountrySerializer(ModelSerializer):
    """国家序列化"""

    class Meta:
        model = Country
        fields = ['id', 'name', 'name_en']
