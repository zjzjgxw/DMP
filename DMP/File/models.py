import os
import datetime
import uuid
from django.db import models
from rest_framework import serializers


def upload_file_to(instance, filename):
    ext = filename.split('.')[-1]
    file_name = '{}.{}'.format(uuid.uuid4().hex, ext)
    file_path = os.path.join(instance.module, datetime.datetime.now().strftime('%Y/%m/%d/'))
    file_name = ''.join([file_path, file_name])
    return file_name


class Files(models.Model):
    name = models.CharField("文件名称", max_length=50, default="")
    type = models.PositiveSmallIntegerField("文件存储方式，1为本地，2为oss", default=0)
    module = models.CharField("模块名称", max_length=50, default="common")
    path = models.FileField("文件存储路径", upload_to=upload_file_to, max_length=250)
    created_at = models.DateTimeField("产生时间", auto_now_add=True)

    class Meta:
        db_table = 'files'


class FilesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = ['id', 'name', 'type', 'module', 'path']
