from DMP.Business.Models.Vendor import VendorSerializer
from DMP.Core.Service import BasicService
from DMP.Core.Exceptions import ValidationException
from django.db import transaction, IntegrityError


class VendorService(BasicService):
    """
    供应商服务
    """

    @classmethod
    def create(cls, **kwargs):
        """
        创建供应商
        :param kwargs:
        :return:
        """
        serializer = VendorSerializer(data=kwargs)
        if serializer.is_valid():
            vendor = serializer.save()
            return vendor.id
        else:
            raise ValidationException(detail=serializer.errors)
