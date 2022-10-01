import pickle
from .models import Configuration
from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, "default.html", {"title_of_page": "Index Page",
                                            "number_off_stock": 1})

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
    
    result = serializers.serialize('json', all_items, fields=('key','value', "HasActive"))

    return JsonResponse(result, safe=False)