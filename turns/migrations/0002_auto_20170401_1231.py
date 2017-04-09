# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turns', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turn',
            name='player',
            field=models.ForeignKey(related_name='turn_player', to='players.Player'),
        ),
        migrations.AlterField(
            model_name='turn',
            name='target',
            field=models.ForeignKey(related_name='turn_target', to='players.Player'),
        ),
    ]
