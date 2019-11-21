from DMP.Business.Views.BusinessViewSet import BusinessViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'business', BusinessViewSet, base_name="businessView")

urlpatterns = router.urls
