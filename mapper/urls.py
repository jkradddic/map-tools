"""buzzmaps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from rest_framework import routers

from api import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/maps/$', views.map_list),
    url(r'^api/maps/(?P<pk>[0-9]+)/$', views.map_detail),
    url(r'^bpage$', TemplateView.as_view(template_name='bpage.html')),
    url(r'^cms$', TemplateView.as_view(template_name='cms.html')),
    url(r'^maps/(?P<map_id>[0-9]+)/$', TemplateView.as_view(template_name='map.html')),
    url(r'^gallery$', TemplateView.as_view(template_name='gallery.html')),
    url(r'^demo/test$', TemplateView.as_view(template_name='demo/test.html')),
    url(r'^creator-test$', TemplateView.as_view(template_name='creator-test.html')),

]
