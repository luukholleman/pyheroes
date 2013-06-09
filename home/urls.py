from django.conf.urls import patterns, include, url
from home.views import HomeTemplateView

urlpatterns = patterns('',
    url(r'^$', HomeTemplateView.as_view(), name='home'),
    url(r'^home/([a-zA-Z]+)$', HomeTemplateView.as_view(), name='home.ranklist'),
)