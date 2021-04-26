from django.db import models
from ckeditor.fields import RichTextField
from profiles.models import Profile

# Create your models here.


class Report(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='reports/', blank=True)
    remarks = RichTextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.CharField(max_length=200)

    def __str__(self):
        return self.name
