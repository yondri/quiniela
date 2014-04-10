from django.conf.urls import patterns, include, url
from quiniela.views import current_datetime
from quiniela.views import plus

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'quiniela.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', plus),
)