# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cyclist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('secondlastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.PositiveIntegerField()),
                ('birthday', models.DateField()),
                ('created', models.DateField(auto_now_add=True)),
                ('phone', models.CharField(max_length=50)),
                ('category', models.CharField(default=b'P', max_length=1, choices=[(b'P', b'Principiante'), (b'I', b'Intermedia'), (b'A', b'Avanzada')])),
                ('alias', models.CharField(max_length=50)),
                ('club', models.CharField(max_length=50)),
                ('emergency_phone', models.CharField(max_length=50)),
                ('contact_name', models.CharField(max_length=50)),
                ('contact_phone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('created', models.DateField(auto_now_add=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('cost', models.DecimalField(max_digits=10, decimal_places=3)),
                ('distance', models.DecimalField(max_digits=10, decimal_places=2)),
                ('category', models.CharField(default=b'P', max_length=1, choices=[(b'P', b'Principiante'), (b'I', b'Intermedia'), (b'A', b'Avanzada')])),
                ('limit', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Jersey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total', models.PositiveIntegerField(default=0)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('event', models.ForeignKey(to='core.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Medal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total', models.PositiveIntegerField(default=0)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('event', models.ForeignKey(to='core.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Suscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.PositiveIntegerField()),
                ('jersey', models.BooleanField(default=False)),
                ('medal', models.BooleanField(default=False)),
                ('ride', models.BooleanField(default=False)),
                ('size', models.CharField(default=b'L', max_length=1, choices=[(b'S', b'Small'), (b'M', b'Medium'), (b'L', b'Large'), (b'XL', b'X Large'), (b'XXL', b'XX Large')])),
                ('package', models.CharField(default=b'U', max_length=1, choices=[(b'D', b'Entregado'), (b'U', b'Pendiente')])),
                ('status', models.CharField(default=b'U', max_length=1, choices=[(b'A', b'Accepted'), (b'P', b'In Process')])),
                ('cyclist', models.ForeignKey(to='core.Cyclist')),
                ('event', models.ForeignKey(to='core.Event')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
