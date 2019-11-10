from DMP.District.Models.Country import *
from django.core.exceptions import ObjectDoesNotExist


class CountryService:
    errors = None

    def __init__(self):
        pass

    def list(self):
        serializer = CountrySerializer(Country.objects.all(), many=True)
        return serializer.data

    def detail(self, id):
        try:
            country = Country.objects.get(id=id)
        except ObjectDoesNotExist:
            return {}
        serializer = CountrySerializer(country)
        return serializer.data
