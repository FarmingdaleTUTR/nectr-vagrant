# -*- coding: utf-8 -*-
"""nectr-vagrant URL Configuration

https://docs.djangoproject.com/en/1.8/topics/http/urls/

"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings


urlpatterns = [
    url(
        regex=r'^admin/',
        view=include(admin.site.urls)),

    url(
        regex=r'^$',
        view=TemplateView.as_view(template_name='base.html'),
        name="home"),


]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
