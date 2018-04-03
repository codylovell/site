# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Projects

# Create your views here.
def projects(request):
	projects = Projects.objects.all()
	return render(request, 'projects/projects.html', {'projects': projects})