from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pyheroes.views.home', name='home'),
    # url(r'^pyheroes/', include('pyheroes.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('home.urls')),
    url(r'^', include('hero.urls')),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/vagrant/media'}),
    (r'^assets/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/vagrant/assets'}),
)
