from DMP.Business.Models.BasicInfo import BasicInfo, BusinessSerializer
from DMP.Core.Service import BasicService
from DMP.Core.Exceptions import ValidationException
from DMP.Business.Service.UserService import UserService
from django.db import transaction
from django.db import IntegrityError


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
                else:
                    raise ValidationException(detail=serializer.errors)
        except ValidationException:
            raise
        except IntegrityError:
            raise
        return True
