from django.urls import path
from . import views

urlpatterns = [
    path('solicitar-servico/', views.solicitar_servico, name='solicitar-servico'),
    path('', views.index, name='index'),
]
