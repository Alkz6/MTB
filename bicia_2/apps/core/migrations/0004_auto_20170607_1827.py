# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170607_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suscription',
            name='size',
            field=models.CharField(default=b'L', max_length=3, choices=[(b'S', b'Small'), (b'M', b'Medium'), (b'L', b'Large'), (b'XL', b'X Large'), (b'XXL', b'XX Large')]),
        ),
    ]
