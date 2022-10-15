from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('c/index', views.configuration_index, name ="c_index"),
    path('c/lst', views.configuration, name ="allConfiguration"),
    path('c/add', views.configuration_add, name ="add"),
    path('c/edit', views.configuration_edit, name ="edit"),
    path('c/del', views.configuration_del, name ="del"),
]