from .Place import *
from rest_framework.serializers import ModelSerializer


class State(Place):
    country = models.ForeignKey('Country', db_constraint=False, related_name='states',
                                on_delete=models.SET_DEFAULT,
                                default=0)


class StateSerializer(ModelSerializer):
    """国家序列化"""

    class Meta:
        model = State
        fields = ['id', 'name', 'name_en', 'country_id']
