from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'gathering_data_index.html')