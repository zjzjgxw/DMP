from DMP.Business.Models.User import UserSerializer
from DMP.Core.Service import BasicService
from DMP.Core.Exceptions import ValidationException


class UserService(BasicService):
    """
    用户服务
    """

    @classmethod
    def create_admin_user(cls, email, business):
        """
        创建管理员账户
        :param email:
        :param business:
        :return:
        """
        serializer = UserSerializer(data={"account": email, "business": business.id})
        if serializer.is_valid():
            user = serializer.save()
        else:
            raise ValidationException(serializer.errors)
        return True
