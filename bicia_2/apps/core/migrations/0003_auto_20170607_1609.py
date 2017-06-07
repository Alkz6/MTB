# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170607_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jersey',
            name='event',
        ),
        migrations.RemoveField(
            model_name='medal',
            name='event',
        ),
        migrations.AddField(
            model_name='event',
            name='jerseys',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='left_jerseys',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='left_medals',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='left_suscriptions',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='medals',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cyclist',
            name='email',
            field=models.EmailField(max_length=254, db_index=True),
        ),
        migrations.AlterField(
            model_name='cyclist',
            name='lastname',
            field=models.CharField(max_length=50, db_index=True),
        ),
        migrations.AlterUniqueTogether(
            name='suscription',
            unique_together=set([('event', 'number'), ('event', 'cyclist')]),
        ),
        migrations.DeleteModel(
            name='Jersey',
        ),
        migrations.DeleteModel(
            name='Medal',
        ),
    ]
