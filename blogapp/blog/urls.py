from .views import HomeView, AboutView, ProjectView
from django.urls import path

# app_name = 'blog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('project', ProjectView.as_view(), name='project'),
    path('about', AboutView.as_view(), name='about'),   
]