from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url('', 'naught.views.index',name='naught-index', prefix='')    
)