from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'stock_analysis.html')

def stock_analysis(request):
    return