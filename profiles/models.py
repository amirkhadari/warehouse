from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = RichTextField()
    avatar = models.ImageField(upload_to='user_profile/',
                               default='no_picture.png')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def get_user_name(self):
        return self.user.username

    def __str__(self):
        return self.user.username
