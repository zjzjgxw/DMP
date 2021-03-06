from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from DMP.Helps.func import return_format
from DMP.Core.Token import auth_permission_required
from DMP.Product.Service.StockService import StockService
from DMP.Core.Exceptions import ValidationException
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

    @auth_permission_required(['stock_info'])
    def retrieve(self, request, pk=None):
        data = StockService.detail(pk)
        return Response(return_format(200, data=data))

    @auth_permission_required(['stock_info_update'])
    def update(self, request, pk=None):
        res = StockService.update(pk, **request.data)
        return Response(return_format(200, data={"res": res}))

    def partial_update(self, request, pk=None):
        pass

