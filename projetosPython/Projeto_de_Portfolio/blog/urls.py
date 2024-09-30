from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='postagem_list'),
    path('postagem/<int:pk>/', views.post_detail, name='postagem_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('youtube_videos/', views.get_youtube_videos, name='youtube_videos'),
]
