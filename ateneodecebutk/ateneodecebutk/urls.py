from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'ateneodecebutk.views.index', name='index'),
    url(r'^ict/doc/', include('django.contrib.admindocs.urls')),
    url(r'^ict/', include(admin.site.urls)),
    url(r'^gradebook/', include('gradebook.urls', namespace='gradebook')),
    url(r'^downloads/', include('downloads.urls', namespace='downloads')),
)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
