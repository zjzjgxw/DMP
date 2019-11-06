from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField("名称", max_length=30, default="")
    name_en = models.CharField("英文名称", max_length=50, default="")
    created_at = models.DateTimeField("日志产生时间", auto_now_add=True)
    created_at = models.DateTimeField("日志修改时间", auto_now=True)

    class Meta:
        abstract = True


class Country(Place):
    class Meta:
        db_table = 'district_country'


class State(Place):
    country = models.ForeignKey('Country', db_constraint=False, related_name='state_country',
                                on_delete=models.SET_DEFAULT,
                                default=0)


class City(Place):
    country = models.ForeignKey('Country', db_constraint=False, related_name='city_country',
                                on_delete=models.SET_DEFAULT,
                                default=0)
    state = models.ForeignKey('State', db_constraint=False, related_name='city_state', on_delete=models.SET_DEFAULT,
                              default=0)
