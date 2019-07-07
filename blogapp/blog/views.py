from django.shortcuts import render
from django.views.generic import TemplateView, YearArchiveView, CreateView, UpdateView, DeleteView
from .models import MyBlogModel 
from .forms import MyBlogForm

class HomeView(TemplateView, YearArchiveView):
    template_name = 'home.html'
    object_list = MyBlogModel.objects.all()
    model = MyBlogModel
    date_field = "pub_date"
    year_format = '%Y'
    allow_future = False
    year = 2019

class CreatePostView():
    template_name = 'post.html'
    form_class = MyBlogForm

class UpdatePostView():
    template_name = 'update.html'
    form_class = MyBlogForm

class DeletePostView():
    template_name = 'delete.html'
    form_class = MyBlogForm

