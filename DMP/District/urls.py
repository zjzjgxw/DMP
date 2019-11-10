from DMP.District.Views.CountryView import *
from DMP.District.Views.StateView import *
from DMP.District.Views.CityView import *

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'country', CountryView, base_name="country")
router.register(r'country/(?P<country_id>\d+)/state', StateView, base_name="state")
router.register(r'country/(?P<country_id>\d+)/state/(?P<state_id>\d+)/city', CityView, base_name="state")


urlpatterns = router.urls
