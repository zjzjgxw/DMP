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

    @classmethod
    def verify(cls, pk, vendor_id):
        """
        审核合同
        :param pk:
        :param vendor_id:
        :return:
        """
        try:
            obj = VendorContract.objects.get(pk=pk, vendor=vendor_id)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExistException()
        return obj.verify()

    @classmethod
    def refuse(cls, pk, vendor_id):
        """
        拒绝审核
        :param pk:
        :param vendor_id:
        :return:
        """
        try:
            obj = VendorContract.objects.get(pk=pk, vendor=vendor_id)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExistException()
        return obj.refuse()

    @classmethod
    def approve(cls, pk, vendor_id):
        """
        通过审核
        :param pk:
        :param vendor_id:
        :return:
        """
        try:
            obj = VendorContract.objects.get(pk=pk, vendor=vendor_id)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExistException()
        return obj.approve()

    @classmethod
    def invalid(cls, pk, vendor_id):
        """
        作废合同
        :param pk:
        :param vendor_id:
        :return:
        """
        try:
            obj = VendorContract.objects.get(pk=pk, vendor=vendor_id)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExistException()
        return obj.invalid()
