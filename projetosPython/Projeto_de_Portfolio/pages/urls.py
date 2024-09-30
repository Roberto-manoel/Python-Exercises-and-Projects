from django.urls import path
from . import views

urlpatterns = [
    path('redes_sociais/', views.get_redes_sociais, name='redes_sociais'),
    path('home/', views.get_home, name='home'),
    path('', views.get_site, name='site'),
    path('tech_news/', views.get_tech_news, name='tech_news'),
]
