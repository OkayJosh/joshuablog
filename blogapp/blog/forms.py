from django import forms
from markdownx.fields import MarkdownxFormField
from .models import MyBlogModel

class MyBlogForm(forms.ModelForm):
    class Meta:
        models = MyBlogModel
        fields = ['title', 'Post', 'pub_date']