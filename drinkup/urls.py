from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'drinkup.views.view_base'),
    url(r'^about/$', 'drinkup.views.view_about'),
    url(r'^past/$', 'drinkup.views.view_past'),
    url(r'^admin/', include(admin.site.urls)),
)