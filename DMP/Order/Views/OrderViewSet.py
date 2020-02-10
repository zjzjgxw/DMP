from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from DMP.Helps.func import return_format
from DMP.Core.Token import auth_permission_required
from DMP.Core.Paginate import PagePaginate
from DMP.Order.Service.OrderService import OrderService


class OrderViewSet(ViewSet):
    """
    订单视图
    """

    @auth_permission_required(["order_list"])
    def list(self, request):
        business_id = request.dmp_user['business_id']
        page_paginate = PagePaginate(request)
        data = OrderService.list(business_id, page_paginate.page, page_paginate.page_size)
        return Response(return_format(200, data=data))

    @auth_permission_required(["order_create"])
    def create(self, request):
        business_id = request.dmp_user['business_id']
        vendor_id = OrderService.create(business_id, **request.data)
        return Response(return_format(200, data={"id": vendor_id}))

    @auth_permission_required(['order_detail'])
    def retrieve(self, request, pk=None):
        business_id = request.dmp_user['business_id']
        data = OrderService.detail(business_id, pk)
        return Response(return_format(200, data=data))

    @auth_permission_required(['order_update'])
    def update(self, request, pk=None):
        business_id = request.dmp_user['business_id']
        res = OrderService.update(business_id, pk, **request.data)
        return Response(return_format(200, data={"res": res}))

    def partial_update(self, request, pk=None):
        pass

    @auth_permission_required(['order_delete'])
    def destroy(self, request, pk=None):
        business_id = request.dmp_user['business_id']
        res = OrderService.delete(business_id, pk)
        return Response(return_format(200, data={"res": res}))
