# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe

from markdown_deux import markdown


class Post(models.Model):
	'''Post model'''
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)


	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def get_markdown(self):
		text = self.text
		markdown_text = markdown(text)
		return mark_safe(markdown_text)


	def __str__(self):
		return self.title



class Comment(models.Model):
	'''Comment model -- related name field allows for access to comments
	from within post model.'''
	post = models.ForeignKey('blog.Post', related_name='comments')
	author = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	approved_comment = models.BooleanField(default=False)


	def approve(self):
		self.approved_comment = True
		self.save()


	def __str__(self):
		return self.text

