from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from DMP.BusinessLog.service.LogService import LogService
from django.http import QueryDict
from rest_framework.request import Request


class LogViewSet(ViewSet):
    """
    业务日志类
    """

    def list(self, request):
        return Response("heesslo")

    def create(self, request):
        params = request.data
        res = LogService.create(models_name=params['models_name'], record_id=params['record_id'],
                                user_name=params['user_name'], behavior_type=params['behavior_type'],
                                content=params['content'])
        return Response(res)

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

    def __get_parameter_dic(self, request):
        if isinstance(request, Request):
            return {}

        query_params = request.query_params
        if isinstance(query_params, QueryDict):
            query_params = query_params.dict()
        result_data = request.data
        if isinstance(result_data, QueryDict):
            result_data = result_data.dict()

        if query_params != {}:
            return query_params
        else:
            return result_data
