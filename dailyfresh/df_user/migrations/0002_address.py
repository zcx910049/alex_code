# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('create_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('recipient_name', models.CharField(verbose_name='收件人', max_length=24)),
                ('recipient_addr', models.CharField(verbose_name='收件地址', max_length=256)),
                ('recipient_phone', models.CharField(verbose_name='联系电话', max_length=11)),
                ('zip_code', models.CharField(verbose_name='邮政编码', max_length=6)),
                ('is_default', models.BooleanField(default=False, verbose_name='是否默认')),
                ('passport', models.ForeignKey(to='df_user.Passport', verbose_name='所属账户')),
            ],
            options={
                'db_table': 's_user_address',
            },
        ),
    ]
