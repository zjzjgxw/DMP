from DMP.Business.Views.BusinessViewSet import BusinessViewSet
from DMP.Business.Views.BusinessAuthInfoViewSet import BusinessAuthInfoViewSet
from DMP.Business.Views.UserViewSet import UserViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'business', BusinessViewSet, base_name="businessView")
router.register(r'auth', BusinessAuthInfoViewSet, base_name="businessAuthInfoView")
router.register(r'user', UserViewSet, base_name="userView")

urlpatterns = router.urls
