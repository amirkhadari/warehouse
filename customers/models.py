from django.db import models
# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='customers/',
                             default='no_picture.png')
    slug = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
