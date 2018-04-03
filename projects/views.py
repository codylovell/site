# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect

from .models import Project

# Create your views here.
def projects(request):
	projects = Project.objects.all()
	context = {'projects': projects}
	return render(request, 'projects/projects.html', context)


def project_detail(request, pk):
	project = get_object_or_404(Project, pk=pk)
	context = {'project': project}
	return render(request, 'projects/project_detail.html', context)