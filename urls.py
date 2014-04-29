from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'testflavors.views.home'),
    url(r'^get-departements/(?P<region>[0-9]{2})/$', 'testflavors.views.get_departements'),
)

