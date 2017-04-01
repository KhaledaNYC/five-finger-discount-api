# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phases', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phase',
            name='winner',
            field=models.ForeignKey(related_name='phase_winner', to='players.Player'),
        ),
    ]
