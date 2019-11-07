from .Place import *


class City(Place):
    country = models.ForeignKey('Country', db_constraint=False, related_name='city_country',
                                on_delete=models.SET_DEFAULT,
                                default=0)
    state = models.ForeignKey('State', db_constraint=False, related_name='city_state', on_delete=models.SET_DEFAULT,
                              default=0)
