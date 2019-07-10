from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, YearArchiveView, CreateView, UpdateView, DeleteView
from .models import MyBlogModel 
from .forms import MyBlogForm

class HomeView(TemplateView):
    template_name = 'home.html'
    model = MyBlogModel

class AboutView(TemplateView):
    template_name = 'about.html'
    model = MyBlogModel

class ProjectView(TemplateView):
    template_name = 'project.html'
    model = MyBlogModel

