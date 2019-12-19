from django.db import models
from rest_framework import serializers
from DMP.Business.Models.Vendor import Vendor


class VendorBankAccount(models.Model):
    """
    供应商银行账户信息
    """
    IN_COUNTRY = 1
    OUT_COUNTRY = 2
    ACCOUNT_TYPE_CHOICES = (
        (IN_COUNTRY, '境内'),
        (OUT_COUNTRY, '境外')
    )

    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, db_column='business_vendor_id',
                               db_constraint=False)
    account_type = models.PositiveSmallIntegerField("账户类型", choices=ACCOUNT_TYPE_CHOICES, default=IN_COUNTRY)
    company_name = models.CharField("收款单位名称", max_length=250, default="")
    company_address = models.CharField("收款单位地址", max_length=250, default="")
    bank_name = models.CharField("开户银行名称", max_length=250, default="")
    bank_address = models.CharField("开户银行地址", max_length=250, default="")
    bank_account = models.CharField("开户银行账户", max_length=30, default="")
    swift_code = models.CharField("switf code", max_length=250, default="")
    district_code = models.CharField("收款人常驻国家（地区）名称及代码", max_length=250, default="")
    delete_flag = models.PositiveSmallIntegerField("删除标记", default=0)
    created_at = models.DateTimeField("产生时间", auto_now_add=True)
    updated_at = models.DateTimeField("修改时间", auto_now=True)

    class Meta:
        db_table = 'business_vendor_bank_account'


class VendorBankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorBankAccount
        fields = ['id', 'vendor', 'account_type', "company_name", "company_address", "bank_name", "bank_address",
                  "bank_account", "swift_code",
                  "district_code"]
        extra_kwargs = {'account_type': {'required': True}, 'company_name': {'required': True},
                        'company_address': {'required': True}, 'bank_name': {'required': True},
                        'bank_address': {'required': True}, 'bank_account': {'required': True},
                        "vendor": {'required': True}}
