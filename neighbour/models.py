from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import Q
import datetime as dt

Priority=(
    ('Informative','Informative'),
    ('High Priority','High Priority'),
)

# Create your models here.
class Neighbourhood(models.Model):
    hood= models.CharField(max_length=100)

    def __str__(self):
        return self.hood

    def save_hood(self):
        self.save()

    @classmethod
    def delete_hood(cls,Neighbourhood):
        cls.objects.filter(Neighbourhood=Neighbourhood).delete()


class Notifications(models.Model):
    title = models.CharField(max_length=100)
    notification = HTMLField()
    priority = models.CharField(max_length=15,choices=Priority,default="Informative")
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Healthservices(models.Model):
    healthservices = models.CharField(max_length=100)

    def __str__(self):
        return self.healthservices

    def save_healthservices(self):
        self.save()

    @classmethod
    def delete_healthservices(cls,Healthservices):
        cls.objects.filter(Healthservices=Healthservices).delete()


class Business(models.Model):
    logo = models.ImageField(upload_to='businesslogo/')
    description = HTMLField()
    hood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    address =models.CharField(max_length=100)
    contact = models.IntegerField()

    def __str__(self):
        return self.name

class Health(models.Model):
    logo = models.ImageField(upload_to='healthlogo/')
    hood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address =models.CharField(max_length=100)
    healthservices = models.ManyToManyField(Healthservices)

    def __str__(self):
        return self.name

class Authorities(models.Model):
    hood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address =models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatars/')
    description = HTMLField()
    hood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='post/')
    post = HTMLField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    hood= models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to='avatars/')

    def __str__(self):
        return self.title

    @classmethod
    def search_blog(cls,search_term):
        blogs = cls.objects.filter(Q(username__username=search_term) | Q(Neighbourhood__Neighbourhood=search_term) | Q(title__icontains=search_term))
        return blogs


class Comment(models.Model):
    comment = models.CharField(max_length=300)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Blog,on_delete=models.CASCADE)
