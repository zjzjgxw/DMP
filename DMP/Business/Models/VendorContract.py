from django.db import models
from rest_framework import serializers
from DMP.Business.Models.Vendor import Vendor
from DMP.Business.Models.VendorBankAccount import VendorBankAccount
from DMP.Core.Paginate import PageManager


class ContractStatus:
    """
    合同状态
    """
    instance = None
    code = None

    def __init__(self, instance):
        """
        :param instance: VendorContract
        """
        self.instance = instance

    def verify(self):
        """
        审核合同
        :return:
        """
        pass

    def refuse(self):
        """
        拒绝合同
        :return:
        """
        pass

    def approve(self):
        """
        批准
        :return:
        """
        pass

    def invalid(self):
        """
        作废
        :return:
        """
        pass


class InvalidStatus(ContractStatus):
    """
    失效状态
    """
    code = 3

    def verify(self):
        self.instance.set_status(self.instance.verifying_status)


class VerifyingStatus(ContractStatus):
    """
    审核中状态
    """
    code = 1

    def refuse(self):
        self.instance.set_status(self.instance.verify_failed_status)

    def approve(self):
        self.instance.set_status(self.instance.valid_status)


class VerifyFailedStatus(ContractStatus):
    """
    审核失败状态
    """
    code = 4

    def verify(self):
        self.instance.set_status(self.instance.verifying_status)


class ValidStatus(ContractStatus):
    """
    有效状态
    """
    code = 2

    def invalid(self):
        self.instance.set_status(self.instance.invalid_status)


class VendorContract(models.Model):
    """
    供应商合同信息
    """
    MAIN_CONTRACT = 1  # 主合同
    APPEND_CONTRACT = 2  # 补充协议
    CONTRACT_TYPE_CHOICES = (
        (MAIN_CONTRACT, '主合同'),
        (APPEND_CONTRACT, '补充协议')
    )

    CYCLE_PAY = 1  # 按周期结算
    ORDER_PAY = 2  # 按单结算
    PAY_TYPE_CHOICES = (
        (CYCLE_PAY, '周期结算'),
        (ORDER_PAY, '单结算')
    )

    CONTRACT_STATUS_CHOICES = (
        (VerifyingStatus.code, '审核中'),
        (ValidStatus.code, '有效'),
        (InvalidStatus.code, '失效的'),
        (VerifyFailedStatus.code, '审核失败'),
    )

    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, db_column='business_vendor_id',
                               db_constraint=False)
    contract_type = models.PositiveSmallIntegerField("合同类型", choices=CONTRACT_TYPE_CHOICES, default=MAIN_CONTRACT)
    name = models.CharField("合同名称", max_length=250, default="")
    file_id = models.BigIntegerField("合同文件id", default=0)
    sign_date = models.DateField("签约日期", default="")
    expired_date = models.DateField("到期日期", default="")
    bank_account = models.ForeignKey(VendorBankAccount, on_delete=models.CASCADE, db_column='bank_count_id',
                                     db_constraint=False)
    pay_type = models.PositiveSmallIntegerField("结算类型", choices=PAY_TYPE_CHOICES, default=CYCLE_PAY)
    pay_currency_code = models.CharField("付款币种", max_length=3, default="CNY")
    offer_currency_code = models.CharField("报价币种", max_length=3, default="CNY")
    status = models.PositiveSmallIntegerField("合同状态", choices=CONTRACT_STATUS_CHOICES, default=VerifyFailedStatus.code)
    delete_flag = models.PositiveSmallIntegerField("删除标记", default=0)
    created_at = models.DateTimeField("产生时间", auto_now_add=True)
    updated_at = models.DateTimeField("修改时间", auto_now=True)
    objects = PageManager()

    current_status = InvalidStatus

    def __init__(self, *args, **kwargs):
        super(VendorContract, self).__init__(*args, **kwargs)
        self.invalid_status = InvalidStatus(self)
        self.valid_status = ValidStatus(self)
        self.verifying_status = VerifyingStatus(self)
        self.verify_failed_status = VerifyFailedStatus(self)
        self.status_map = {self.invalid_status.code: self.invalid_status, self.valid_status.code: self.valid_status,
                           self.verify_failed_status.code: self.verify_failed_status,
                           self.verifying_status.code: self.verifying_status}
        self.current_status = self.status_map[self.status]

    def set_status(self, obj: ContractStatus):
        self.current_status = obj
        self.status = obj.code

    class Meta:
        db_table = 'business_vendor_contract'


class VendorContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorContract
        fields = ['id', 'vendor', 'contract_type', "name", "file_id", "sign_date", "expired_date",
                  "bank_account", "pay_type", "pay_currency_code", "offer_currency_code", "status"]
        extra_kwargs = {'contract_type': {'required': True}, 'name': {'required': True},
                        'file_id': {'required': True}, 'sign_date': {'required': True},
                        'expired_date': {'required': True}, 'bank_account': {'required': True},
                        'pay_type': {'required': True}, 'pay_currency_code': {'required': True},
                        'offer_currency_code': {'required': True}}
