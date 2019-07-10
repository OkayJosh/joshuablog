from django.contrib import admin

from markdownx.admin import MarkdownxModelAdmin
from .models import MyBlogModel

admin.site.register(MyBlogModel, MarkdownxModelAdmin)