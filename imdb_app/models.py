# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from decimal import Decimal
# Create your models here.


class Genre(models.Model):
	title = models.CharField(max_length=30, unique=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('title',)



class Movies(models.Model):
	movie_name = models.CharField(max_length=50)
	director_name = models.CharField(max_length=50, blank=True, 
									null=True)
	imdb_score = models.DecimalField(max_digits=11, decimal_places=2,
									default=Decimal('0.00'), blank=True, 
									null=True)
	popularity_score = models.DecimalField(max_digits=11, decimal_places=2,
										default=Decimal('0.00'),blank=True, 
										null=True)
	genre_type = models.ManyToManyField(Genre, default="")

	def __str__(self):
		return self.movie_name

	class Meta:
		ordering = ('movie_name',)


