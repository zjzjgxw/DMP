from DMP.Business.Models.BasicInfo import BasicInfo, BusinessSerializer
from DMP.Core.Service import BasicService


class BusinessService(BasicService):
    """
    商户服务
    """

    @classmethod
    def create(cls, **kwargs):
        """
        创建
        :param kwargs:
        :return:
        """
        serializer = BusinessSerializer(data=kwargs)
        if serializer.is_valid():
            serializer.save()
        else:
            cls.errors = serializer.errors
            cls.error_code = 10001
            return False
        return True
