from django.db import models


# Create your models here.
class BasicInfo(models):
    name = models.CharField("商户名称", max_length=30, default="")
    created_at = models.DateTimeField("日志产生时间", auto_now_add=True)
    updated_at = models.DateTimeField("日志修改时间", auto_now=True)
