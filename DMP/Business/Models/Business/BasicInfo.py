from django.db import models


class BasicInfo(models):
    """
    商户基础信息表
    """
    name = models.CharField("商户名称", max_length=30, default="")
    logo_img_id = models.BigIntegerField("头像文件id", default=0)
    tel = models.CharField("联系电弧", max_length=30, default="")
    delete_flag = models.PositiveSmallIntegerField("删除标记", default=0)
    created_at = models.DateTimeField("日志产生时间", auto_now_add=True)
    updated_at = models.DateTimeField("日志修改时间", auto_now=True)
