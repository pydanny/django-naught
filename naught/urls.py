from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url('^dot/$', 'naught.views.dot', name='naught-graph'),
    url('^$', 'naught.views.index', name='naught-index'),
)