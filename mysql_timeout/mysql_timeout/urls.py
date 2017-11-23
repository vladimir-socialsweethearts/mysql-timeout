"""mysql_timeout URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import logging

from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from django.db import connection
from django.contrib.auth.models import User
import time

TIMEOUT = 2
logger = logging.getLogger('main')


def home(request):
    with connection.cursor() as cursor:
        cursor.execute('SHOW VARIABLES')
        logger.info(cursor.fetchone())
        time.sleep(TIMEOUT)
        cursor.execute('SHOW VARIABLES')
        logger.info(cursor.fetchone())
    return HttpResponse('foo')


def home2(request):
    index = request.GET.get('index', '')
    logger.info('Task {}'.format(index))
    list(User.objects.all())
    time.sleep(TIMEOUT)
    list(User.objects.all())
    return HttpResponse('foo')


def home3(request):
    user = email = password = str(int(time.time()))
    User.objects.create_superuser(user, email, password)
    time.sleep(TIMEOUT)
    user = email = password = str(int(time.time()))
    User.objects.create_superuser(user, email, password)
    return HttpResponse('foo')


def home4(request):
    User.objects.get(id=1)
    time.sleep(TIMEOUT)
    User.objects.get(id=1)
    return HttpResponse('foo')


urlpatterns = [
    url(r'^$', home),
    url(r'^test2', home2),
    url(r'^test3', home3),
    url(r'^test4', home4),
    url(r'^admin/', admin.site.urls),
]
