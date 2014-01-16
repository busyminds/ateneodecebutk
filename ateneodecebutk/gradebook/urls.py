from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^G[1-6][A-G]-[A-Z]{2,3}$', views.detail, name='details')
)
