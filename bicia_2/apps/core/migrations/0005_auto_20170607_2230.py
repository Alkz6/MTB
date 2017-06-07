# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20170607_1827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cyclist',
            old_name='alias',
            new_name='nickname',
        ),
        migrations.AlterField(
            model_name='event',
            name='cost',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='suscription',
            name='size',
            field=models.CharField(default=b'N', max_length=3, choices=[(b'N', b'None'), (b'S', b'Small'), (b'M', b'Medium'), (b'L', b'Large'), (b'XL', b'X Large'), (b'XXL', b'XX Large')]),
        ),
    ]
