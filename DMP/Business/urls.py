from DMP.Business.Views.BusinessViewSet import BusinessViewSet
from DMP.Business.Views.BusinessAuthInfoViewSet import BusinessAuthInfoViewSet
from DMP.Business.Views.UserViewSet import UserViewSet
from DMP.Business.Views.DepartmentViewSet import DepartmentViewSet
from DMP.Business.Views.PermissionRoleViewSet import PermissionRoleViewSet
from DMP.Business.Views.VendorViewSet import VendorViewSet
from DMP.Business.Views.VendorBankAccountViewSet import VendorBankAccountViewSet
from DMP.Business.Views.VendorContractViewSet import VendorContractViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'business', BusinessViewSet, base_name="BusinessView")
router.register(r'auth', BusinessAuthInfoViewSet, base_name="BusinessAuthInfoView")
router.register(r'user', UserViewSet, base_name="UserView")
router.register(r'department', DepartmentViewSet, base_name="DepartmentView")
router.register(r'permission_role', PermissionRoleViewSet, base_name="PermissionRoleView")
router.register(r'vendor', VendorViewSet, base_name="VendorView")
router.register(r'vendor_bank_account', VendorBankAccountViewSet, base_name="VendorBankAccountView")
router.register(r'vendor_contract', VendorContractViewSet, base_name="VendorContractView")

urlpatterns = router.urls
