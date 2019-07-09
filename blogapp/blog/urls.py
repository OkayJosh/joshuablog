from .views import HomeView, CreatePostView
from django.urls import path

# app_name = 'blog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create', CreatePostView.as_view(), name='create'),
    
]