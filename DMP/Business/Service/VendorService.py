from DMP.Business.Models.Vendor import VendorSerializer, Vendor
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

    @classmethod
    def list(cls, business_id, page=1, page_size=10):
        count = Vendor.objects.count(business_id)
        vendor_list = Vendor.objects.list(business_id, page, page_size)
        serializer = VendorSerializer(vendor_list, many=True)
        return {"list": serializer.data, "count": count}
