from DMP.Business.Models.User import UserSerializer, User, UserRoleRelation
from DMP.Business.Models.Department import DepartmentUserRelation
from DMP.Core.Service import BasicService
from DMP.Core.Exceptions import ValidationException, UserNotExistException, AccountPasswordWrongException, \
    PermissionFailException
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

        serializer = UserSerializer(data={"account": email, "business": business_id, "name": "admin", "is_admin": 1,
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
            token = jwt.get_token(id=user.id, name=user.name, account=user.account, business_id=user.business_id,
                                  is_admin=user.is_admin, is_active=user.is_active)
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

    @classmethod
    def list(cls, business_id, page=1, page_size=10):
        count = User.objects.count(business_id)
        user_list = User.objects.list(business_id, page, page_size)
        serializer = UserSerializer(user_list, many=True)
        return {"list": serializer.data, "count": count}

    @classmethod
    def update(cls, user_id, business_id, **kwargs):
        """
        用户信息修改
        :param user_id:
        :param business_id:
        :param kwargs:
        :return:
        """
        try:
            user = User.objects.get(pk=user_id, business_id=business_id)
        except ObjectDoesNotExist:
            raise UserNotExistException()

        try:
            with transaction.atomic("BusinessMysql"):
                serializer = UserSerializer(user, kwargs, partial=True)
                if serializer.is_valid():
                    serializer.save()
                else:
                    raise ValidationException(detail=serializer.errors)
                if "role_ids" in kwargs:
                    if not isinstance(kwargs["role_ids"], list):
                        raise ValidationException(10007)
                    new_role_ids = set(kwargs["role_ids"])
                    cls._update_role_relation(user_id, new_role_ids)
                if "department_ids" in kwargs:
                    if not isinstance(kwargs["department_ids"], list):
                        raise ValidationException(10007)
                    new_department_ids = set(kwargs["department_ids"])
                    cls._update_department_relation(user_id, new_department_ids)
        except IntegrityError:
            raise
        return True

    @classmethod
    def _update_department_relation(cls, user_id, new_department_ids):
        """
        更新用户-部门关系
        :param user_id:
        :param new_department_ids:
        :return:
        """
        query_set = DepartmentUserRelation.objects.filter(user_id=user_id).values("department_id")
        department_ids = set()
        for item in query_set:
            department_ids.add(item["department_id"])
        if department_ids != new_department_ids:
            DepartmentUserRelation.objects.filter(user_id=user_id).delete()
            query_set_list = []
            for new_id in new_department_ids:
                query_set_list.append(DepartmentUserRelation(user_id=user_id, department_id=new_id))
            DepartmentUserRelation.objects.bulk_create(query_set_list)

    @classmethod
    def _update_role_relation(cls, user_id, new_role_ids):
        """
        更新用户-职位关系
        :param user_id:
        :param new_role_ids:
        :return:
        """
        query_set = UserRoleRelation.objects.filter(user_id=user_id).values("role_id")
        role_ids = set()
        for item in query_set:
            role_ids.add(item["role_id"])
        if role_ids != new_role_ids:
            UserRoleRelation.objects.filter(user_id=user_id).delete()
            query_set_list = []
            for new_id in new_role_ids:
                query_set_list.append(UserRoleRelation(user_id=user_id, role_id=new_id))
            UserRoleRelation.objects.bulk_create(query_set_list)

    @classmethod
    def detail(cls, user_id, business_id):
        try:
            user = User.objects.get(pk=user_id, business_id=business_id)
        except ObjectDoesNotExist:
            raise UserNotExistException()
        serializer = UserSerializer(user)
        data = serializer.data
        query_set = UserRoleRelation.objects.filter(user_id=user_id)
        data["role_ids"] = []
        for item in query_set:
            data["role_ids"].append(item.role_id)
        query_set = DepartmentUserRelation.objects.filter(user_id=user_id)
        data["departments"] = []
        for item in query_set:
            data["departments"].append(item.department_id)
        return data

    @classmethod
    def has_permissions(cls, user_id: int, permissions: list):
        query_set = UserRoleRelation.objects.filter(user_id=user_id)
        permission_set = set()
        for item in query_set:
            role = item.role
            for permission in role.permissions.all():
                permission_set.add(permission.name)
        for item in permissions:
            if item not in permission_set:
                raise PermissionFailException()
        return True
