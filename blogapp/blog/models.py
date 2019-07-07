from django.db import models
from markdownx.models import MarkdownxField
from django.template.defaultfilters import slugify

class MyBlogModel(models.Model):
    title = models.CharField(max_length=200)
    post = MarkdownxField()
    slug = models.SlugField()
    pub_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(MyBlogModel, self).save(*args, **kwargs)


    def __str__(self):
        return self.title

