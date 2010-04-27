from warnings import warn

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db.models import fields
from django.db.models.fields.related import ForeignKey
from django.db.models import get_app, get_models
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def make_apps():

    apps = []
    for app_name in settings.INSTALLED_APPS:


        try:        
            app_module = get_app(app_name)            
            app_models = get_models(app_module)
        except ImproperlyConfigured, e:
            warn(str(e))
            continue
            
        models = []
        for app_model in app_models:
            model = {
                'model':app_model
            }
            fields = app_model._meta.fields
            for field in fields:
                if isinstance(field, ForeignKey):
                    field.related = True
            model['fields'] = fields
            models.append(model)                
        app = {
            'app_name':app_name,
            'app_module':app_module,
            'models':models,

        }
        apps.append(app)
        
    return apps
    
def dot(request):
    graph = ''    
    apps = make_apps()
    for i, app in enumerate(apps):
        if not app['models']:
            continue
        graph += 'subcluster_%s {\n' % i
        
        for j, model in enumerate(app['models']):
            graph += 'model_%s_%s [label="%s"]\n' % (i, j, str(model['model']))
        
        graph += '}\n'

    return HttpResponse(graph)

def index(request):
    
    return render_to_response('naught/index.html',
            { 'apps':make_apps() },
            context_instance=RequestContext(request))