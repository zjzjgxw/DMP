from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from DMP.Helps.func import return_format
from DMP.Core.Token import auth_permission_required
from DMP.Core.Paginate import PagePaginate
from DMP.Product.Service.DetailService import DetailService


class DetailViewSet(ViewSet):
    """
    商品详情视图
    """

    @auth_permission_required(["product_detail_list"])
    def list(self, request):
        business_id = request.dmp_user['business_id']
        page_paginate = PagePaginate(request)
        name = None
        category_id = None
        status_type = None
        if "name" in request.data:
            name = request.data['name']
        if "category_id" in request.data:
            category_id = request.data['category_id']
        if "status_type" in request.data:
            status_type = request.data['status_type']
        data = DetailService.list(business_id=business_id, name=name, category_id=category_id, status_type=status_type,
                                  page=page_paginate.page, page_size=page_paginate.page_size)
        return Response(return_format(200, data=data))

    @auth_permission_required(["product_detail_create"])
    def create(self, request):
        business_id = request.dmp_user['business_id']
        detail_id = DetailService.create(business_id, **request.data)
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
