import pickle
from .models import Configuration
from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, "default.html", {"title_of_page": "Index Page",
                                            "number_off_stock": 1})

# Create your views here.
def news(request):
    return render(request, "default.html", {"title_of_page": "Index Page",
                                            "number_off_stock": 1})

@csrf_exempt
def configuration_index(request):
    context = {
        "title_of_page": "Configuration"
    }
    return render(request, "configuration.html", context)

def configuration(request):
    all_items = Configuration.objects.all()

    """ result=[]
    for item in config_list:
        result.append({'key':item.key, 'value':item.value, 'HasActive':item.HasActive}) """
    
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