from DMP.Business.Models.User import UserSerializer
from DMP.Core.Service import BasicService
from DMP.Core.Exceptions import ValidationException
from django.contrib.auth.hashers import make_password


class UserService(BasicService):
    """
    用户服务
    """

    @classmethod
    def create_admin_user(cls, email, business_id):
        """
        创建管理员账户
        :param email:
        :param business_id:
        :return:
        """
        password = '123456'

        serializer = UserSerializer(data={"account": email, "business": business_id,
                                          'password': make_password(password)})
        if serializer.is_valid():
            serializer.save()
        else:
            raise ValidationException(serializer.errors)
        return True
