from DMP.BusinessLog.models import *
from datetime import datetime


class LogService:
    """
    日志服务类
    """
    errors = None

    def __init__(self, models_name):
        self.models_name = models_name
        self.error_info = None

    def create(self, record_id, user_name, behavior_type, content):
        """
        新建日志
        :param record_id:
        :param user_name:
        :param behavior_type:
        :param content:
        :return:
        """
        serializer = LogSerializer(
            data={"models_name": self.models_name, "record_id": record_id, "behavior_type": behavior_type,
                  "user_name": user_name,
                  "content": content,
                  'record_time': datetime.now()})
        if serializer.is_valid():
            serializer.create(serializer.data)
            return True
        self.errors = 10001
        self.error_info = serializer.errors
        return False

    def list(self, record_id=None):
        """
        获取日志列表
        :param record_id:
        :return:
        """
        query_set = Log.objects.filter(models_name=self.models_name)
        if record_id:
            query_set = query_set.filter(record_id=record_id)
        serializer = LogSerializer(query_set, many=True)
        return serializer.data
