from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from DMP.Helps.func import return_format
from rest_framework.decorators import action
from DMP.Business.Service.UserService import UserService
from DMP.Core.Token import auth_permission_required
from DMP.Core.Paginate import PagePaginate
from DMP.Business.Service.VendorService import VendorService


class VendorViewSet(ViewSet):
    """
    供应商视图
    """

    @auth_permission_required(["vendor_list"])
    def list(self, request):
        business_id = request.dmp_user['business_id']
        page_paginate = PagePaginate(request)
        result = UserService.list(business_id, page_paginate.page, page_paginate.page_size)
        return Response(return_format(200, data=result))

    @auth_permission_required(["vendor_list"])
    def create(self, request):
        business_id = request.dmp_user['business_id']
        vendor_id = VendorService.create(**request.data, business=business_id)
        return Response(return_format(200, data={"id": vendor_id}))

    @auth_permission_required(['user_detail'])
    def retrieve(self, request, pk=None):
        business_id = request.dmp_user['business_id']
        data = UserService.detail(pk, business_id)
        return Response(return_format(200, data=data))

    @auth_permission_required(['user_update'])
    def update(self, request, pk=None):
        business_id = request.dmp_user['business_id']
        UserService.update(pk, business_id, **request.data)
        return Response(return_format(200))

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
