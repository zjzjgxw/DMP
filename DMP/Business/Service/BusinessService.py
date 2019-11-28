from DMP.Business.Models.BasicInfo import BusinessSerializer
from DMP.Core.Service import BasicService
from DMP.Core.Exceptions import ValidationException
from DMP.Business.Service.UserService import UserService
from django.db import transaction
from django.db import IntegrityError
from DMP.Business.Models.BusinessAuthInfo import BusinessAuthInfoSerializer


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
        try:
            with transaction.atomic('BusinessMysql'):
                serializer = BusinessSerializer(data=kwargs)
                if serializer.is_valid():
                    business = serializer.save()
                    UserService.create_admin_user(business.email, business.id)
                    return business.id
                else:
                    raise ValidationException(detail=serializer.errors)
        except ValidationException:
            raise
        except IntegrityError:
            raise

    @classmethod
    def auth(cls, **kwargs):
        """
        提交认证信息
        :param kwargs:
        :return:
        """
        kwargs['business'] = kwargs['business_id']
        serializer = BusinessAuthInfoSerializer(data=kwargs)
        if serializer.is_valid():
            serializer.save()
        else:
            raise ValidationException(detail=serializer.errors)
        return True
