from DMP.File.views import FileViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'files', FileViewSet, base_name="files")


urlpatterns = router.urls
