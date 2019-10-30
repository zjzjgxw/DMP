from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from DMP.BusinessLog.models import Log
from datetime import datetime


class LogViewSet(ViewSet):
    """
    业务日志类
    """

    def list(self, request):
        return Response("heesslo")

    def create(self, request):
        log = Log(models_name="test", record_id=2, behavior_type=2, user_name='gxw', content="gxxx",
                  record_time=datetime.now())
        log.save()
        return Response("heesssssslo")

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
