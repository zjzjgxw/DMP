from DMP.District.Views.CountryView import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'country', CountryView, base_name="country")

urlpatterns = router.urls
