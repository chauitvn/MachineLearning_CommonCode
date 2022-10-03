from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='f_index'),
    path('f/stock_analysis', views.stock_analysis, name='f_stock_analysis_index'),
]