# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib import admin
from .views import show_news
from .views import NewsView, ArticleList

admin.autodiscover()

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', NewsView.as_view(), name='news_category'),
    url(r'^(?P<myid>\d+)/like/$', show_news, name='show'),
    url(r'^rule/$', ArticleList.as_view(), name='rule'),
    url(r'^list/$', ArticleList.as_view(), name='list'),
]