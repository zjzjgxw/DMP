from DMP.Product.Views.CategoryViewSet import CategoryViewSet
from DMP.Product.Views.DetailViewSet import DetailViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'category', CategoryViewSet, base_name="CategoryView")
router.register(r'product_detail', DetailViewSet, base_name="ProductDetailView")

urlpatterns = router.urls
