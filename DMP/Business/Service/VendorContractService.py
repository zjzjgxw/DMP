from DMP.Business.Models.VendorContract import VendorContract, VendorContractSerializer
from DMP.Core.Service import BasicService
from django.core.exceptions import ObjectDoesNotExist
from DMP.Core.Exceptions import ValidationException, ObjectDoesNotExistException


class VendorContractService(BasicService):
    """
    供应商合同
    """

    @classmethod
    def create(cls, **kwargs):
        """
        创建供应商银行账户
        :param kwargs:
        :return:
        """
        serializer = VendorContractSerializer(data=kwargs)
        if serializer.is_valid():
            obj = serializer.save()
            return obj.id
        else:
            raise ValidationException(detail=serializer.errors)

    @classmethod
    def list(cls, vendor_id, page=1, page_size=10):
        count = VendorContract.objects.count(vendor_id=vendor_id)
        contract_list = VendorContract.objects.list(page, page_size, vendor_id=vendor_id)
        serializer = VendorContractSerializer(contract_list, many=True)
        return {"list": serializer.data, "count": count}

    @classmethod
    def detail(cls, pk, vendor_id):
        try:
            obj = VendorContract.objects.get(pk=pk, vendor=vendor_id)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExistException()
        serializer = VendorContractSerializer(obj)
        return serializer.data

    @classmethod
    def update(cls, pk, vendor_id, **kwargs):
        try:
            obj = VendorContract.objects.get(pk=pk, vendor=vendor_id)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExistException()
        serializer = VendorContractSerializer(obj, kwargs, partial=True)
        if serializer.is_valid():
            serializer.save()
            return True
        else:
            raise ValidationException(detail=serializer.errors)

    @classmethod
    def delete(cls, pk, vendor_id):
        try:
            obj = VendorContract.objects.get(pk=pk, vendor=vendor_id)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExistException()
        obj.delete_flag = 1
        obj.save()
        return True
