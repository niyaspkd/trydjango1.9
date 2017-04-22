"""trydjango19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url

from posts.views import (
	post_list,
	post_create,
	post_edit,
	post_delete,
	post_detail,)

urlpatterns = [
    
    url(r'^list/$', post_list, name="list"),
    url(r'^create/$', post_create, name="create"),
    url(r'^(?P<id>\d+)/edit/$', post_edit, name="edit"),
    url(r'^detail/(?P<id>\d+)/$', post_detail, name="detail"),
    url(r'^(?P<id>\d+)/delete/$', post_delete, name="delete"),

    
]
