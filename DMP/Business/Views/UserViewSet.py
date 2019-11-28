from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from DMP.Helps.func import return_format
from rest_framework.decorators import action
from DMP.Core.Exceptions import ValidationException
from DMP.Business.Service.UserService import UserService


class UserViewSet(ViewSet):
    """
    用户视图
    """

    def list(self, request):
        pass

    def create(self, request):
        pass

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
        res = UserService.login(request.data['account'], request.data['password'])
        return Response(return_format(200, data=res))
