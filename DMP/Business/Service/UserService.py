from DMP.Business.Models.User import UserSerializer, User, UserRoleRelation
from DMP.Business.Models.Department import DepartmentUserRelation
from DMP.Core.Service import BasicService
from DMP.Core.Exceptions import ValidationException, UserNotExistException, AccountPasswordWrongException
from django.core.exceptions import ObjectDoesNotExist
from DMP.Core.Token import JwtToken
from django.db import transaction, IntegrityError


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
                                          'password': password})
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
        res = user.check_password(password)
        if res:
            jwt = JwtToken()
            token = jwt.get_token(id=user.id, name=user.name, account=user.account, business_id=user.business_id)
            return token
        else:
            raise AccountPasswordWrongException()

    @classmethod
    def create_user(cls, **kwargs):
        """
        创建用户
        :param kwargs:
        :return:
        """
        exist = User.objects.filter(account=kwargs["account"]).exists()
        if exist:
            raise ValidationException(10008)
        try:
            with transaction.atomic('BusinessMysql'):
                serializer = UserSerializer(data=kwargs)
                if serializer.is_valid():
                    user = serializer.save()
                else:
                    raise ValidationException(detail=serializer.errors)
                department_ids = kwargs["department_ids"]
                role_ids = kwargs["role_ids"]
                query_set_list = []
                for role_id in role_ids:
                    query_set_list.append(UserRoleRelation(user_id=user.id, role_id=role_id))
                UserRoleRelation.objects.bulk_create(query_set_list)
                query_set_list = []
                for department_id in department_ids:
                    query_set_list.append(DepartmentUserRelation(department_id=department_id, user_id=user.id))
                DepartmentUserRelation.objects.bulk_create(query_set_list)
                return user.id
        except IntegrityError:
            raise
