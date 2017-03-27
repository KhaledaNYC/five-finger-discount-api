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
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rounds_to_win', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('game', models.ForeignKey(related_name='phase_game', to='FiveFingerDiscountAPI.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField(default=0)),
                ('game', models.ForeignKey(related_name='score_game', to='FiveFingerDiscountAPI.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Turn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eliminated', models.BooleanField()),
                ('draw', models.ForeignKey(related_name='turn_draw', to='FiveFingerDiscountAPI.Card')),
                ('end_hand', models.ForeignKey(related_name='turn_end_hand', to='FiveFingerDiscountAPI.Card')),
                ('phase', models.ForeignKey(related_name='turn_phase', to='FiveFingerDiscountAPI.Phase')),
                ('played', models.ForeignKey(related_name='turn_played', to='FiveFingerDiscountAPI.Card')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('avatar', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.AddField(
            model_name='turn',
            name='player',
            field=models.ForeignKey(related_name='turn_player', to='FiveFingerDiscountAPI.User'),
        ),
        migrations.AddField(
            model_name='turn',
            name='start_hand',
            field=models.ForeignKey(related_name='turn_card', to='FiveFingerDiscountAPI.Card'),
        ),
        migrations.AddField(
            model_name='turn',
            name='target',
            field=models.ForeignKey(related_name='turn_target', to='FiveFingerDiscountAPI.User'),
        ),
        migrations.AddField(
            model_name='score',
            name='player',
            field=models.ForeignKey(related_name='score_player', to='FiveFingerDiscountAPI.User'),
        ),
        migrations.AddField(
            model_name='phase',
            name='winner',
            field=models.ForeignKey(related_name='phase_winner', to='FiveFingerDiscountAPI.User'),
        ),
        migrations.AddField(
            model_name='game',
            name='winner',
            field=models.ForeignKey(related_name='game_winner', to='FiveFingerDiscountAPI.User'),
        ),
    ]
