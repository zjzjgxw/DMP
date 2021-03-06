# Generated by Django 2.1.7 on 2019-11-19 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30, verbose_name='名称')),
                ('name_en', models.CharField(default='', max_length=50, verbose_name='英文名称')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='日志产生时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='日志修改时间')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30, verbose_name='名称')),
                ('name_en', models.CharField(default='', max_length=50, verbose_name='英文名称')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='日志产生时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='日志修改时间')),
            ],
            options={
                'db_table': 'district_country',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30, verbose_name='名称')),
                ('name_en', models.CharField(default='', max_length=50, verbose_name='英文名称')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='日志产生时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='日志修改时间')),
                ('country', models.ForeignKey(db_constraint=False, default=0, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='states', to='District.Country')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(db_constraint=False, default=0, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='city_country', to='District.Country'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(db_constraint=False, default=0, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='cities', to='District.State'),
        ),
    ]
