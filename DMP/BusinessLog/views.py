from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from DMP.BusinessLog.service.LogService import LogService
from DMP.Helps.func import return_format


class LogViewSet(ViewSet):
    """
    业务日志类
    """

    def list(self, request):
        params = request.data
        if 'models_name' not in params:
            return Response(return_format(10001))
        if 'record_id' not in params:
            params["record_id"] = None
        service = LogService(models_name=params['models_name'])
        return Response(service.list(params["record_id"]))

    def create(self, request):
        params = request.data
        service = LogService(models_name=params['models_name'])
        res = service.create(record_id=params['record_id'],
                             user_name=params['user_name'], behavior_type=params['behavior_type'],
                             content=params['content'])
        if res:
            return Response(return_format())
        return Response(return_format(service.errors))

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
