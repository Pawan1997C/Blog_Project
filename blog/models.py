from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length = 100)


    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    image = models.ImageField(default = 'programming.jpg', upload_to = 'blog_pics')
    category = models.ForeignKey(Category, null = True, on_delete = models.SET_NULL)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default= 'default.jpg', upload_to = 'profile_pics')

    def __str__(self):
        return self.user.username

