# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('imdb_app', '0003_auto_20180131_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='imdb_score',
            field=models.DecimalField(default=Decimal('0.00'), null=True, max_digits=11, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='popularity_score',
            field=models.DecimalField(default=Decimal('0.00'), null=True, max_digits=11, decimal_places=2, blank=True),
        ),
    ]
