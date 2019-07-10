from django.db import models
from markdownx.models import MarkdownxField
from django.template.defaultfilters import slugify
from markdownx.utils import markdownify

class MyBlogModel(models.Model):
    CATEGORY = (
    ('AR', 'Article'),
    ('TA', 'Talks'),
    ('PR', 'Projects'),
                            )
    title = models.CharField(max_length=200)
    created_by = models.CharField(max_length=200, default='etentlabs')
    # blog_type = models.CharField(max_length=10, choices=CATEGORY), 
    post = MarkdownxField()
    slug = models.SlugField( null=True, blank=True)
    pub_date = models.DateTimeField()

    def formatted_markdown(self):
        return markdownify(self.post)

    def body_summary(self):
        return markdownify(self.post[:300] + "...")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(MyBlogModel, self).save(*args, **kwargs)


    def __str__(self):
        return self.title

