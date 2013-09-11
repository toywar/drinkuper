from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',)

urlpatterns = patterns('drinkuper.drinkup.views',
    # Examples:
    # url(r'^$', 'drinkuper.views.home', name='home'),
    url(r'^$', include('drinkup.urls')),
    #url(r'^about/$', include('drinkup.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)