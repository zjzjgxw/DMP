from .views import LogViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'logs', LogViewSet, base_name="logs")

urlpatterns = router.urls
