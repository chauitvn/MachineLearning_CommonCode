from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('news', views.news, name="news"),
    path('c/index', views.configuration_index, name='c_index'),
    path('c/lst', views.configuration, name ="allConfiguration")
]