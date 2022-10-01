from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('c/index', views.configuration_index, name='c_index'),
    path('c/lst', views.configuration, name ="allConfiguration")
]