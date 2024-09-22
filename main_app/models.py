from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=100)
    info = models.TextField()
    image = models.ImageField(upload_to='about/')
    icon = models.ImageField(upload_to='about-icon/')
    icon_title = models.CharField(max_length=100)
    icon_info = models.TextField()

    def __str__(self):
        return self.title


class Shop(models.Model):
    image = models.ImageField(upload_to='shops/')
    title = models.CharField(max_length=100)
    info = models.TextField()
    price = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Service(models.Model):
    icon = models.ImageField(upload_to='service-icon/')
    title = models.CharField(max_length=100)
    info = models.TextField()

    def __str__(self):
        return self.title


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog-images/')
    info = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

