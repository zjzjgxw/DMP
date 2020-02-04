from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from DMP.Helps.func import return_format
from DMP.Core.Token import auth_permission_required
from DMP.Product.Service.StockService import StockService
import time

class StockViewSet(ViewSet):
    """
    库存视图
    """

    @auth_permission_required(["product_detail_list"])
    def list(self, request):
        # business_id = request.dmp_user['business_id']
        # page_paginate = PagePaginate(request)
        # data = CategoryService.list(business_id, page_paginate.page, page_paginate.page_size)
        time.sleep(10)
        return Response(return_format(200))

    @auth_permission_required(["stock_create"])
    def create(self, request):
        detail_id = StockService.create(**request.data)
        return Response(return_format(200, data={"id": detail_id}))

    @auth_permission_required(['product_detail_info'])
    def retrieve(self, request, pk=None):
        business_id = request.dmp_user['business_id']
        data = DetailService.detail(business_id, pk)
        return Response(return_format(200, data=data))

    @auth_permission_required(['product_detail_update'])
    def update(self, request, pk=None):
        business_id = request.dmp_user['business_id']
        res = DetailService.update(business_id, pk, **request.data)
        return Response(return_format(200, data={"res": res}))

    def partial_update(self, request, pk=None):
        pass

    @auth_permission_required(['product_detail_delete'])
    def destroy(self, request, pk=None):
        business_id = request.dmp_user['business_id']
        res = DetailService.delete(business_id, pk)
        return Response(return_format(200, data={"res": res}))
