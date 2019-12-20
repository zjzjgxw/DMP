from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from DMP.Helps.func import return_format
from DMP.Core.Token import auth_permission_required
from DMP.Core.Paginate import PagePaginate
from DMP.Core.Exceptions import ValidationException
from DMP.Business.Service.VendorBankAccountService import VendorBankAccountService


class VendorBankAccountViewSet(ViewSet):
    """
    供应商视图
    """

    @auth_permission_required(["vendor_bank_account_list"])
    def list(self, request):
        if "vendor_id" not in request.data:
            raise ValidationException()
        vendor_id = request.data["vendor_id"]
        if not isinstance(vendor_id, int):
            raise ValidationException(10009)
        page_paginate = PagePaginate(request)
        result = VendorBankAccountService.list(vendor_id, page_paginate.page, page_paginate.page_size)
        return Response(return_format(200, data=result))

    @auth_permission_required(["vendor_bank_account_list"])
    def create(self, request):
        bank_account_id = VendorBankAccountService.create(**request.data)
        return Response(return_format(200, data={"id": bank_account_id}))

    @auth_permission_required(['vendor_detail'])
    def retrieve(self, request, pk=None):
        if "vendor_id" not in request.data:
            raise ValidationException()
        vendor_id = request.data["vendor_id"]
        if not isinstance(vendor_id, int):
            raise ValidationException(10009)
        data = VendorBankAccountService.detail(pk, vendor_id)
        return Response(return_format(200, data=data))

    @auth_permission_required(['vendor_update'])
    def update(self, request, pk=None):
        if "vendor_id" not in request.data:
            raise ValidationException()
        vendor_id = request.data["vendor_id"]
        del request.data["vendor_id"]
        if not isinstance(vendor_id, int):
            raise ValidationException(10009)
        VendorBankAccountService.update(pk, vendor_id, **request.data)
        return Response(return_format(200))

    def partial_update(self, request, pk=None):
        pass

    @auth_permission_required(['vendor_delete'])
    def destroy(self, request, pk=None):
        if "vendor_id" not in request.data:
            raise ValidationException()
        vendor_id = request.data["vendor_id"]
        if not isinstance(vendor_id, int):
            raise ValidationException(10009)
        VendorBankAccountService.delete(pk, vendor_id)
        return Response(return_format(200))
