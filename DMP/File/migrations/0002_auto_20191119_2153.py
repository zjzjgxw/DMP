# Generated by Django 2.1.7 on 2019-11-19 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('File', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='module',
            field=models.CharField(default='common', max_length=50, verbose_name='模块名称'),
        ),
        migrations.AlterModelTable(
            name='files',
            table='files',
        ),
    ]
