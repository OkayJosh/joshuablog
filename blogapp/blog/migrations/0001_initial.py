# Generated by Django 2.2.2 on 2019-07-10 19:20

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyBlogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_by', models.CharField(default='etentlabs', max_length=200)),
                ('post', markdownx.models.MarkdownxField()),
                ('slug', models.SlugField()),
                ('pub_date', models.DateTimeField()),
            ],
        ),
    ]
