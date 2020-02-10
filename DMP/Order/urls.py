from DMP.Order.Views.OrderViewSet import OrderViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'order', OrderViewSet, base_name="OrderView")

urlpatterns = router.urls
