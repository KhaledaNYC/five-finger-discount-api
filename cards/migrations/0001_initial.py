# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
                ('rank', models.IntegerField()),
                ('image', models.ImageField(upload_to=b'')),
                ('action', models.CharField(max_length=30)),
            ],
        ),
    ]
