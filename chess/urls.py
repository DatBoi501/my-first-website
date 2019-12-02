from django.urls import path
from . import views

urlpatterns = [
    path('', views.info_list, name='info_list'),
]
