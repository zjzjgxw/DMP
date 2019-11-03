from django.db import models
from rest_framework.serializers import ModelSerializer, ValidationError


# Create your models here.
class Log(models.Model):
    id = models.BigAutoField(primary_key=True)
    models_name = models.CharField("模块名", max_length=30, default="")
    record_id = models.BigIntegerField("被记录的实体id", default=0)
    user_name = models.CharField("操作用户名", max_length=30, default='')
    behavior_type = models.PositiveSmallIntegerField("操作类型，1为新增，2为修改，3为删除", default=0)
    content = models.TextField("日志内容", default="")
    record_time = models.DateTimeField("业务记录时间")
    create_time = models.DateTimeField("日志产生时间", auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['models_name', 'record_id']),
        ]


class LogSerializer(ModelSerializer):
    """日志序列化器"""

    def validate_models_name(self, models_name):
        if len(models_name) > 10:
            raise ValidationError("模块名太长")
        return models_name

    class Meta:
        model = Log
        fields = '__all__'
