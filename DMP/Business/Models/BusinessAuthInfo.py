from django.db import models

from DMP.Business.Models.BasicInfo import BasicInfo


class BusinessAuthInfo(models.Model):
    """
    商户认证信息表
    """
    COMPANY_SIZE_CHOICES = (
        (1, '1~10人'),
        (2, '10~50人'),
        (3, '50~100人'),
        (4, '100~500人'),
        (5, '500以上'),
    )

    business = models.OneToOneField(BasicInfo, on_delete=models.SET_NULL, db_column='business_basic_id',
                                    db_constraint=False)
    name = models.CharField("企业名", max_length=30, default="")
    unique_code = models.CharField("企业统一编码", max_length=30, default="")
    img_id = models.BigIntegerField("企业营业执照文件id", default=0)
    web = models.URLField("网址", default="")
    linkman = models.CharField("联系人姓名", max_length=50, default="")
    linkman_tel = models.CharField("联系人电话", max_length=30, default="")
    company_size = models.PositiveSmallIntegerField("企业规模", choices=COMPANY_SIZE_CHOICES, default=1)
    main_sales = models.TextField("主营业务", default="")
    country_id = models.PositiveIntegerField("国家id", default=0)
    state_id = models.PositiveIntegerField("省份id", default=0)
    city_id = models.PositiveIntegerField("城市id", default=0)
    address = models.CharField("详细地址", max_length=200, default="")
    created_at = models.DateTimeField("产生时间", auto_now_add=True)
    updated_at = models.DateTimeField("修改时间", auto_now=True)

    class Meta:
        db_table = 'business_auth'
