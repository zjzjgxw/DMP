from django.db import models
from rest_framework import serializers
from DMP.Business.Models.Vendor import Vendor
from DMP.Business.Models.VendorBankAccount import VendorBankAccount


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

    STATUS_AUDITING = 1  # 审核中
    STATUS_VALID = 2  # 有效的
    STATUS_INVALID = 3  # 失效的
    STATUS_AUDIT_FAILED = 4  # 审核失败

    CONTRACT_STATUS_CHOICES = (
        (STATUS_AUDITING, '审核中'),
        (STATUS_VALID, '有效'),
        (STATUS_INVALID, '失效的'),
        (STATUS_AUDIT_FAILED, '审核失败'),
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
    status = models.PositiveSmallIntegerField("合同状态", choices=CONTRACT_STATUS_CHOICES, default=STATUS_INVALID)
    delete_flag = models.PositiveSmallIntegerField("删除标记", default=0)
    created_at = models.DateTimeField("产生时间", auto_now_add=True)
    updated_at = models.DateTimeField("修改时间", auto_now=True)

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
