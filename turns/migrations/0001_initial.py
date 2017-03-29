# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phases', '0001_initial'),
        ('users', '0001_initial'),
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eliminated', models.BooleanField()),
                ('draw', models.ForeignKey(related_name='turn_draw', to='cards.Card')),
                ('end_hand', models.ForeignKey(related_name='turn_end_hand', to='cards.Card')),
                ('phase', models.ForeignKey(related_name='turn_phase', to='phases.Phase')),
                ('played', models.ForeignKey(related_name='turn_played', to='cards.Card')),
                ('player', models.ForeignKey(related_name='turn_player', to='users.User')),
                ('start_hand', models.ForeignKey(related_name='turn_card', to='cards.Card')),
                ('target', models.ForeignKey(related_name='turn_target', to='users.User')),
            ],
        ),
    ]
