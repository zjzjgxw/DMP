from django.db import models
from DMP.Business.Models.BasicInfo import BasicInfo
from DMP.Business.Models.PermissionRole import PermissionRole
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password, check_password


class UserManager(models.Manager):
    _count = -1

    def count(self, business_id):
        self._count = self.filter(business_id=business_id, delete_flag=0).count()
        return self._count

    def get_user_by_account(self, account):
        return self.get(account=account, delete_flag=0)

    def list(self, business_id, page=1, page_size=10):
        if page < 1:
            page = 1
        bottom = (page - 1) * page_size
        top = bottom + page_size
        if self._count == -1:
            self._count = self.count(business_id)
        if top > self._count:
            top = self._count
        return self.filter(business_id=business_id, delete_flag=0)[bottom: top]


class User(models.Model):
    """
    用户
    """
    UN_KNOW = 0
    MAN = 1
    WOMAN = 2
    SEX_CHOICES = (
        (UN_KNOW, '未知'),
        (MAN, '男'),
        (WOMAN, '女'),
    )

    business = models.ForeignKey(BasicInfo, on_delete=models.CASCADE, db_column='business_basic_id',
                                 db_constraint=False)
    account = models.EmailField("账号名", max_length=100, default="")
    password = models.CharField("密码", max_length=100, default="")
    name = models.CharField("真实姓名", max_length=100, default="")
    entry_date = models.DateField("入职日期")
    last_login = models.DateTimeField("最近登录时间", default='2019-08-04')
    last_ip = models.GenericIPAddressField("最近登录IP", default='')
    login_count = models.PositiveIntegerField("登录次数", default=0)
    sex = models.PositiveSmallIntegerField("性别", choices=SEX_CHOICES, default=UN_KNOW)
    delete_flag = models.PositiveSmallIntegerField("删除标记", default=0)
    is_admin = models.PositiveSmallIntegerField("是否为管理员", default=0)
    is_active = models.PositiveSmallIntegerField("激活标示", default=1)
    created_at = models.DateTimeField("产生时间", auto_now_add=True)
    updated_at = models.DateTimeField("修改时间", auto_now=True)
    permission_roles = models.ManyToManyField(PermissionRole, through='UserRoleRelation',
                                              through_fields=("user", "role"),
                                              )
    objects = UserManager()

    def check_password(self, password):
        if self.is_active == 0:
            return False
        return check_password(password, self.password)


class UserRoleRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_constraint=False, db_column='business_user_id')
    role = models.ForeignKey(PermissionRole, on_delete=models.CASCADE, db_constraint=False,
                             db_column='business_permission_role_id')

    class Meta:
        db_table = 'business_user_role_relation'


class UserSerializer(ModelSerializer):
    def create(self, validated_data):
        user = User(**validated_data)
        user.password = make_password(password=user.password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ['id', 'account', 'password', 'name', 'entry_date', 'last_login', 'last_ip', 'login_count',
                  'sex', 'is_admin', 'is_active', 'business']
        extra_kwargs = {'account': {'required': True}, 'password': {'required': True, 'write_only': True},
                        "name": {'required': True},
                        "entry_date": {'required': True}}
