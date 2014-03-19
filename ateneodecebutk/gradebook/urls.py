from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^([1-4]){1}$', views.index, name='index'),
                       # e.g. /1/G1A-ART = 1st quarter G1A Arts
                       url(r'^([1-4]){1}/(G[1-6]{1}[A-G]{1}-[A-Z]{2,3})$',
                           views.detail,
                           name='detail'
                           ),
                       # e.g. /1/G1/SCI = 1st quarter aggregate
                       url(r'^([1-4]){1}/G([1-6]{1})/([A-Z]{2,3})$',
                           views.subject,
                           name='subject'
                           )
                       )
