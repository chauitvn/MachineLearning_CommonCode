from django.shortcuts import render

# Create your views here.
def index(request):
    stocks = Stock.objects.all()
    return render(request, 'stock_list.html', {"stocks": stocks})