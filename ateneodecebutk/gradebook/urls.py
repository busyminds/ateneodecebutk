from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^([1-4]){1}$', views.index, name='index'),
    url(r'^([1-4]){1}/(G[1-6]{1}[A-G]{1}-[A-Z]{2,3})$', views.detail, name='details')
)
