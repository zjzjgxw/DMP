from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from DMP.Helps.func import return_format
from DMP.Core.Token import auth_permission_required
from DMP.Core.Paginate import PagePaginate
from DMP.Core.Exceptions import ValidationException
from DMP.Business.Service.VendorContractService import VendorContractService


class VendorContractViewSet(ViewSet):
    """
    供应商合同视图
    """

    @auth_permission_required(["vendor_contract_list"])
    def list(self, request):
        if "vendor_id" not in request.data:
            raise ValidationException()
        vendor_id = request.data["vendor_id"]
        if not isinstance(vendor_id, int):
            raise ValidationException(10009)
        page_paginate = PagePaginate(request)
        result = VendorContractService.list(vendor_id, page_paginate.page, page_paginate.page_size)
        return Response(return_format(200, data=result))

    @auth_permission_required(["vendor_contract_list"])
    def create(self, request):
        bank_account_id = VendorContractService.create(**request.data)
        return Response(return_format(200, data={"id": bank_account_id}))

    @auth_permission_required(['vendor_contact_detail'])
    def retrieve(self, request, pk=None):
        if "vendor_id" not in request.data:
            raise ValidationException()
        vendor_id = request.data["vendor_id"]
        if not isinstance(vendor_id, int):
            raise ValidationException(10009)
        data = VendorContractService.detail(pk, vendor_id)
        return Response(return_format(200, data=data))

    @auth_permission_required(['vendor_contract_update'])
    def update(self, request, pk=None):
        if "vendor_id" not in request.data:
            raise ValidationException()
        vendor_id = request.data["vendor_id"]
        del request.data["vendor_id"]
        if not isinstance(vendor_id, int):
            raise ValidationException(10009)
        VendorContractService.update(pk, vendor_id, **request.data)
        return Response(return_format(200))

    def partial_update(self, request, pk=None):
        pass

    @auth_permission_required(['vendor_contract_delete'])
    def destroy(self, request, pk=None):
        if "vendor_id" not in request.data:
            raise ValidationException()
        vendor_id = request.data["vendor_id"]
        if not isinstance(vendor_id, int):
            raise ValidationException(10009)
        VendorContractService.delete(pk, vendor_id)
        return Response(return_format(200))
