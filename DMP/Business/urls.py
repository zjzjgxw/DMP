from DMP.Business.Views.BusinessViewSet import BusinessViewSet
from DMP.Business.Views.BusinessAuthInfoViewSet import BusinessAuthInfoViewSet
from DMP.Business.Views.UserViewSet import UserViewSet
from DMP.Business.Views.DepartmentViewSet import DepartmentViewSet
from DMP.Business.Views.PermissionRoleViewSet import PermissionRoleViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'business', BusinessViewSet, base_name="BusinessView")
router.register(r'auth', BusinessAuthInfoViewSet, base_name="BusinessAuthInfoView")
router.register(r'user', UserViewSet, base_name="UserView")
router.register(r'department', DepartmentViewSet, base_name="DepartmentView")
router.register(r'permission_role', PermissionRoleViewSet, base_name="PermissionRoleView")

urlpatterns = router.urls
