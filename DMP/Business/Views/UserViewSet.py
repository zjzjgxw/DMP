from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from DMP.Helps.func import return_format
from rest_framework.decorators import action
from DMP.Core.Exceptions import ValidationException
from DMP.Business.Service.UserService import UserService
from DMP.Core.Token import auth_permission_required
from DMP.Core.Paginate import PagePaginate


class UserViewSet(ViewSet):
    """
    用户视图
    """

    @auth_permission_required(["user_list"])
    def list(self, request):
        business_id = request.dmp_user['business_id']
        page_paginate = PagePaginate(request)
        result = UserService.list(business_id, page_paginate.page, page_paginate.page_size)
        return Response(return_format(200, data=result))

    @auth_permission_required(["user_create"])
    def create(self, request):
        business_id = request.dmp_user['business_id']
        if "department_ids" not in request.data:
            raise ValidationException()
        if type(request.data["department_ids"]) != list:
            raise ValidationException(10007)
        if "role_ids" not in request.data:
            raise ValidationException()
        if type(request.data["role_ids"]) != list:
            raise ValidationException(10007)
        user_id = UserService.create_user(**request.data, business=business_id)
        return Response(return_format(200, data={"id": user_id}))

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

    @action(methods=["post"], detail=False)
    def login(self, request):
        if "account" not in request.data:
            raise ValidationException(10002)
        if "password" not in request.data:
            raise ValidationException(10003)
        token = UserService.login(request.data['account'], request.data['password'])
        return Response(return_format(200), headers={'Authorization': token})
