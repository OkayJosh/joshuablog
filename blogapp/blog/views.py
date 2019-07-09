from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, YearArchiveView, CreateView, UpdateView, DeleteView
from .models import MyBlogModel 
from .forms import MyBlogForm

class HomeView(TemplateView):
    template_name = 'home.html'
    model = MyBlogModel

class CreatePostView(CreateView):
    template_name = 'create.html'
    model = MyBlogModel
    form_class = MyBlogForm
    success_url = 'home'
    content_type = None

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        instance  = form.save(commit=False)
        instance.created_by = self.request.user
        instance.save()
        self.object = form.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        if self.success_url:
                url = reverse(self.success_url.format(**self.object.__dict__))        
        else:
                try:
                        url = self.object.get_absolute_url()
                except AttributeError:
                        raise ImproperlyConfigured(
                                "No URL to redirect to.  Either provide a url or define"
                                " a get_absolute_url method on the Model.")
                return url

class UpdatePostView():
    template_name = 'update.html'
    form_class = MyBlogForm

class DeletePostView():
    template_name = 'delete.html'
    form_class = MyBlogForm

class AboutView():
    pass

class ArticleView():
    pass

class TalksView():
    pass

class ProjectView():
    pass

