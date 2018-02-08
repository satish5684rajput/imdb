# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('imdb_app', '0002_auto_20180131_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('movie_name', models.CharField(unique=True, max_length=50)),
                ('director_name', models.CharField(unique=True, max_length=50)),
                ('imdb_score', models.DecimalField(default=Decimal('0.00'), max_digits=3, decimal_places=2)),
                ('popularity_score', models.DecimalField(default=Decimal('0.00'), max_digits=3, decimal_places=2)),
            ],
            options={
                'ordering': ('movie_name',),
            },
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ('title',)},
        ),
        migrations.AddField(
            model_name='movies',
            name='genre_type',
            field=models.ManyToManyField(default='', to='imdb_app.Genre'),
        ),
    ]
