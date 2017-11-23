# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('create_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('user_name', models.CharField(max_length=20, verbose_name='用户名')),
                ('password', models.CharField(max_length=40, verbose_name='密码')),
                ('email', models.CharField(max_length=254, verbose_name='邮箱')),
            ],
            options={
                'db_table': 's_user_account',
            },
        ),
    ]
