from .Place import *


class State(Place):
    country = models.ForeignKey('Country', db_constraint=False, related_name='state_country',
                                on_delete=models.SET_DEFAULT,
                                default=0)
