from django.conf.urls import patterns, include, url

urlpatterns = patterns('landing.apps.signups.views',
    url(r'^$', 'home', name='home'),
)
