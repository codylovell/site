# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	image = models.ImageField()
	created_date = models.DateTimeField(default=timezone.now)


	def __str__(self):
		return self.title