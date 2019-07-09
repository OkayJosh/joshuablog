from django import forms
from markdownx.fields import MarkdownxFormField
from .models import MyBlogModel

class MyBlogForm(forms.ModelForm):
    pass
    # class Meta:
    #     model = MyBlogModel
    #     fields = ['title', 'category', 'post', 'pub_date']