from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "default.html", {"title_of_page": "Index Page",
                                            "number_off_stock": 1})