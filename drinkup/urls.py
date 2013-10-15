from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'drinkup.views.base_passed_view'),
    url(r'^about/$', 'drinkup.views.view_about'),
    url(r'^past/$', 'drinkup.views.past_passed_view'),
    url(r'^temp/$', 'drinkup.views.view_temp'),
    url(r'^admin/', include(admin.site.urls)),
)