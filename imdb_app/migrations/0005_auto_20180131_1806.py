# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imdb_app', '0004_auto_20180131_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='director_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
