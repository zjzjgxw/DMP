from DMP.Product.Views.CategoryViewSet import CategoryViewSet
from DMP.Product.Views.DetailViewSet import DetailViewSet
from DMP.Product.Views.StockViewSet import StockViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'category', CategoryViewSet, base_name="CategoryView")
router.register(r'product_detail', DetailViewSet, base_name="ProductDetailView")
router.register(r'stock', StockViewSet, base_name="StockView")

urlpatterns = router.urls
