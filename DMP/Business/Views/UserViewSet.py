from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from DMP.Helps.func import return_format
from rest_framework.decorators import action
from DMP.Core.Exceptions import ValidationException
from DMP.Business.Service.UserService import UserService
from DMP.Core.Token import auth_permission_required


class UserViewSet(ViewSet):
    """
    用户视图
    """
    page = 1
    page_size = 10

    def _init_pagination(self, request):
        if "page" in request.data:
            self.page = request.data["page"]
        if "page_size" in request.data:
            self.page_size = request.data["page_size"]
        if not isinstance(self.page, int):
            raise ValidationException(10009)
        if not isinstance(self.page_size, int):
            raise ValidationException(10009)
        if self.page < 1 or self.page_size <= 0:
            raise ValidationException(10010)

    @auth_permission_required(["user_list"])
    def list(self, request):
        business_id = request.dmp_user['business_id']
        self._init_pagination(request)
        result = UserService.list(business_id, self.page, self.page_size)
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

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

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
