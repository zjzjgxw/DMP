from .views import DistrictViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'district', DistrictViewSet, base_name="district")

urlpatterns = router.urls
