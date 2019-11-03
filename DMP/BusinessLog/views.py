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
        service = LogService()
        return Response(service.list('test'))

    def create(self, request):
        params = request.data
        service = LogService()
        res = service.create(models_name=params['models_name'], record_id=params['record_id'],
                             user_name=params['user_name'], behavior_type=params['behavior_type'],
                             content=params['content'])
        if res:
            return Response(return_format())
        return Response(return_format(20001, data=service.errors))

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
