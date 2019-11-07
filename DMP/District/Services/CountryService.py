from DMP.District.Models.Country import *


class CountryService:
    errors = None

    def __init__(self):
        pass

    def list(self):
        serializer = CountrySerializer(Country.objects.all(), many=True)
        return serializer.data

    def detail(self, id):
        country = Country.objects.get(id=id)
        serializer = CountrySerializer(country)
        return serializer.data
