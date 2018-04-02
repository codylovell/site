# Cody Lovell's official website
A website for personal blogging and project.

## About
- See : https://www.codyLovell.com
- Author : Design & Code by Cody Lovell
- Tech: Django 1.11(python 3.5+), HTML5 & CSS, Bootstrap, JavaScript

## Version
- Last Updated : 2018-4-3
- version 1.0 : 2018-4-3

## References
##### Django third party apps
* [django-Markdown](https://github.com/klen/django_markdown)
* [django-markdown-deux](https://github.com/trentm/django-markdown-deux)
* [django-tagging](https://github.com/brosner/django-tagging)

##### Built with
* HTML & CSS, Javascript
* Framework: Django 1.11

#### Design
* [Material Design Guide](https://material.io/) by Google

## Setting up Development Environment
Git clone this repository in your working directory.
`git clone https://github.com/codylovell/site.git`

## virtualenv
1 - Install new virtual environment
```python
python3 -m venv [name]
```

2 - Activate your virtual environment
```
source [name]/bin/activate
```

3 - Install packages according to requirements.txt
```
pip3 install -r requirements.txt
```

```python
""" Define preview URL. """

from django.conf.urls import url

from .views import preview

urlpatterns = [
    url('preview/$', preview, name='django_markdown_preview'),
]
```
4. DB migration
```
python3 manage.py migrate
```

## Run Development Server
1 - Start the web server by running python manage.py runserver
```
python manage.py runsslserver
```

##Site should be up
1 - Point your webbrowser to 127.0.0.1:8000


readme based on layout of https://github.com/sujinleeme/sujinlee.me/readme.me
