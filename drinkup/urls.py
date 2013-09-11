from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'drinkup.views.view_base'),
    url(r'^about/$', 'drinkup.views.view_about'),
    url(r'^past/$', 'drinkup.views.view_past'),
)