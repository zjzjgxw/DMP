from DMP.BusinessLog.models import *
from datetime import datetime


class LogService:
    """
    日志服务类
    """
    errors = None

    def create(self, models_name, record_id, user_name, behavior_type, content):
        """
        新建日志
        :param models_name:
        :param record_id:
        :param user_name:
        :param behavior_type:
        :param content:
        :return:
        """
        serializer = LogSerializer(
            data={"models_name": models_name, "record_id": record_id, "behavior_type": behavior_type,
                  "user_name": user_name,
                  "content": content,
                  'record_time': datetime.now()})
        if serializer.is_valid():
            serializer.create(serializer.data)
            return True
        self.errors = serializer.errors
        return False

    def list(self, models_name, record_id=None):
        query_set = Log.objects.filter(models_name=models_name)
        serializer = LogSerializer(query_set, many=True)
        return serializer.data
