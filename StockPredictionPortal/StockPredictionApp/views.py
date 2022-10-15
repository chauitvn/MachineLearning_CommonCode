import pickle
from .models import Configuration
from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    template = loader.get_template("default.html")

    context = {
        "app_title":"Stock Prediction",
        "module_name":"Index",
        "title_of_page": "Index Page",
        "number_off_stock": 1
    }

    return HttpResponse(template.render(request, context))

@csrf_exempt
def configuration_index(request):

    template = loader.get_template("configuration.html")

    context = {
        "app_title":"Stock Prediction",
        "module_name":"Configuration",
        "title_of_page": "Configuration"
    }

    return HttpResponse(template.render(context, request))

def configuration(request):
    all_items = Configuration.objects.all()
    
    result = serializers.serialize('json', all_items)

    return JsonResponse(result, safe=False)

def configuration_add(request):
    key = request.POST.get('fields[key]', None)
    value = request.POST.get('fields[value]', None)
    HasActive = request.POST.get('fields[HasActive]', True)

    if HasActive == 'true':
        HasActive = True
    else:
        HasActive = False

    obj = Configuration.objects.create(
        key = key,
        value = value,
        HasActive = HasActive
    )

    item = {
        'pk':obj.id,
        'fields': {
            'key': obj.key,
            'value':obj.value,
            'HasActive':obj.HasActive
        }
    }

    return JsonResponse(item, safe=False)

def configuration_edit(request):
    id = request.POST.get('pk', None)
    key = request.POST.get('fields[key]', None)
    value = request.POST.get('fields[value]', None)
    HasActive = request.POST.get('fields[HasActive]', True)

    if HasActive == 'true':
        HasActive = True
    else:
        HasActive = False

    obj = Configuration.objects.get(id=id)
    obj.key = key
    obj.value = value
    obj.HasActive = HasActive
    obj.save()

    item = {
        'pk':obj.id,
        'fields': {
            'key': obj.key,
            'value':obj.value,
            'HasActive':obj.HasActive
        }
    }

    return JsonResponse(item, safe=False)

def configuration_del(request):
    id = request.POST.get('pk', None)

    Configuration.objects.get(id=id).delete()
    data = {
        'deleted': True
    }

    return JsonResponse(data, safe=False)