from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='products')
    price = models.FloatField(help_text='in INR')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name
