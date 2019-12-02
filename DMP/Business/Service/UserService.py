from DMP.Business.Models.User import UserSerializer, User
from DMP.Core.Service import BasicService
from DMP.Core.Exceptions import ValidationException, UserNotExistException, AccountPasswordWrongException
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ObjectDoesNotExist
from DMP.Core.Token import JwtToken


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

        serializer = UserSerializer(data={"account": email, "business": business_id, "name": "admin",
                                          'password': make_password(
                                              password)})
        if serializer.is_valid():
            serializer.save()
        else:
            raise ValidationException(serializer.errors)
        return True

    @classmethod
    def login(cls, account, password):
        """
        用户登录
        :param account:
        :param password:
        :return:
        """
        try:
            user = User.objects.get_user_by_account(account)
        except ObjectDoesNotExist:
            raise UserNotExistException()
        res = check_password(password, user.password)
        if res:
            jwt = JwtToken()
            token = jwt.get_token(id=user.id, name=user.name, account=user.account, business_id=user.business_id)
            return token
        else:
            raise AccountPasswordWrongException()
