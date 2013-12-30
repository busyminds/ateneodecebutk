from django.conf.urls import patterns, url

from gradebook import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^downloads/$', views.downloads, name='downloads'),
)
