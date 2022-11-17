
from unittest.util import _MAX_LENGTH
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.template.defaultfilters import slugify


class Categories(models.Model):
    
    categoryname = models.CharField(max_length=255)
   
    def __str__(self):
        return self.categoryname

class Posts(models.Model):

    ARTICLE = "ARTICLE"
    PROJECT = "PROJECT"
    PROART_CHOICES = [(ARTICLE, "Article"),(PROJECT, "Project")]

    title = models.CharField(max_length=250, null=False, blank=False) 
    summary = RichTextField(default = '')

    image = models.ImageField(null=True, blank =True) 
    image_description = models.CharField(max_length = 255, blank = True)
    date_posted = models.DateTimeField(auto_now_add = True)
    body = RichTextField(default = '')
    slug = models.SlugField(max_length=255, blank=True, null=True)
    likes = models.IntegerField(default = 0, editable = False,)
    category = models.ForeignKey(Categories, null = True, on_delete = models.PROTECT)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Inventions(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False)
    image = models.ImageField(null=True, blank =True)
    description_of_project = RichTextField(default = '')
    tech_stack = RichTextField(default = '')
    url = models.CharField(max_length=250, null=False, blank=False, default = 'https://github.com/aphxtwin/')
    
    def __str__(self):
        return self.title 