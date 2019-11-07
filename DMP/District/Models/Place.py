from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField("名称", max_length=30, default="")
    name_en = models.CharField("英文名称", max_length=50, default="")
    created_at = models.DateTimeField("日志产生时间", auto_now_add=True)
    updated_at = models.DateTimeField("日志修改时间", auto_now=True)

    class Meta:
        abstract = True
