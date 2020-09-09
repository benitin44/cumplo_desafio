from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calculadora/', views.get_tmc, name='get_tmc')

]