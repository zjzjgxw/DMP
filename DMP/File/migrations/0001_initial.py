# Generated by Django 2.1.7 on 2019-11-18 20:42

import DMP.File.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='文件名称')),
                ('type', models.PositiveSmallIntegerField(default=0, verbose_name='文件存储方式，1为本地，2为oss')),
                ('module', models.CharField(default='default', max_length=50, verbose_name='模块名称')),
                ('path', models.FileField(max_length=250, upload_to=DMP.File.models.upload_file_to, verbose_name='文件存储路径')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='产生时间')),
            ],
        ),
    ]