from django.shortcuts import render
from .models import Configuration
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
    config_list = Configuration.objects.all()

    json=[]
    for item in config_list:
        json.append({'key':item.key, 'value':item.value, 'HasActive':item.HasActive})

    result = {
        "title_of_page": "Configuration",
        "data": config_list
    }

    return JsonResponse(config_list)