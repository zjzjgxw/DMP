from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from DMP.Helps.func import return_format
from DMP.Core.Token import auth_permission_required
from DMP.Core.Paginate import PagePaginate
from DMP.Product.Service.CategoryService import CategoryService


class CategoryViewSet(ViewSet):
    """
    类目视图
    """

    @auth_permission_required(["category_list"])
    def list(self, request):
        business_id = request.dmp_user['business_id']
        page_paginate = PagePaginate(request)
        data = CategoryService.list(business_id, page_paginate.page, page_paginate.page_size)
        return Response(return_format(200, data=data))

    @auth_permission_required(["category_create"])
    def create(self, request):
        business_id = request.dmp_user['business_id']
        vendor_id = CategoryService.create(business_id, **request.data)
        return Response(return_format(200, data={"id": vendor_id}))

    @auth_permission_required(['category_detail'])
    def retrieve(self, request, pk=None):
        business_id = request.dmp_user['business_id']
        data = CategoryService.detail(business_id, pk)
        return Response(return_format(200, data=data))

    @auth_permission_required(['category_update'])
    def update(self, request, pk=None):
        business_id = request.dmp_user['business_id']
        res = CategoryService.update(business_id, pk, **request.data)
        return Response(return_format(200, data={"res": res}))

    def partial_update(self, request, pk=None):
        pass

    @auth_permission_required(['category_delete'])
    def destroy(self, request, pk=None):
        business_id = request.dmp_user['business_id']
        res = CategoryService.delete(business_id, pk)
        return Response(return_format(200, data={"res": res}))
