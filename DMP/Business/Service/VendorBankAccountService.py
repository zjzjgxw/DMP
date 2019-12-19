from DMP.Business.Models.VendorBankAccount import VendorBankAccount, VendorBankAccountSerializer
from DMP.Core.Service import BasicService
from django.core.exceptions import ObjectDoesNotExist
from DMP.Core.Exceptions import ValidationException, ObjectDoesNotExistException


class VendorBankAccountService(BasicService):
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
        serializer = VendorBankAccountSerializer(data=kwargs)
        if serializer.is_valid():
            bank_account = serializer.save()
            return bank_account.id
        else:
            raise ValidationException(detail=serializer.errors)

    @classmethod
    def list(cls, business_id, page=1, page_size=10):
        pass
        # count = Vendor.objects.count(business_id)
        # vendor_list = Vendor.objects.list(business_id, page, page_size)
        # serializer = VendorSerializer(vendor_list, many=True)
        # return {"list": serializer.data, "count": count}

    @classmethod
    def detail(cls, pk, business_id):
        pass
        # try:
        #     vendor = Vendor.objects.get(pk=pk, business_id=business_id)
        # except ObjectDoesNotExist:
        #     raise ObjectDoesNotExistException()
        # serializer = VendorSerializer(vendor)
        # return serializer.data

    @classmethod
    def update(cls, pk, business_id, **kwargs):
        pass
        # try:
        #     vendor = Vendor.objects.get(pk=pk, business_id=business_id)
        # except ObjectDoesNotExist:
        #     raise ObjectDoesNotExistException()
        # serializer = VendorSerializer(vendor, kwargs, partial=True)
        # if serializer.is_valid():
        #     serializer.save()
        #     return True
        # else:
        #     raise ValidationException(detail=serializer.errors)

    @classmethod
    def delete(cls, pk, business_id):
        pass
        # try:
        #     vendor = Vendor.objects.get(pk=pk, business_id=business_id)
        # except ObjectDoesNotExist:
        #     raise ObjectDoesNotExistException()
        # vendor.delete_flag = 1
        # vendor.save()
        # return True
