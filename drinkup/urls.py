from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'drinkup.views.view_base'),
)