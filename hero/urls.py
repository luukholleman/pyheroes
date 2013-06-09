from django.conf.urls import patterns, include, url
from hero.views import HeroDetailView

urlpatterns = patterns('',
    url(r'^profile/hero/(?P<pk>\d+)/([a-zA-Z0-9\- ]+)/([0-9\- ]+)/$', HeroDetailView.as_view(), name='hero.detail'),
    url(r'^profile/ranks/(?P<pk>\d+)/([a-zA-Z0-9\- ]+)/([0-9\- ]+)/$', HeroDetailView.as_view(), name='hero.ranks'),
    url(r'^profile/stats/(?P<pk>\d+)/([a-zA-Z0-9\- ]+)/([0-9\- ]+)/$', HeroDetailView.as_view(), name='hero.stats')
)