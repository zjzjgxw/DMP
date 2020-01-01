from DMP.Product.Views.CategoryViewSet import CategoryViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'category', CategoryViewSet, base_name="CategoryView")

urlpatterns = router.urls
