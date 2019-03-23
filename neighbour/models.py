from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import Q
import datetime as dt

Priority=(
    ('Informational','Informational'),
    ('High Priority','High Priority'),
)

class neighbourhood(models.Model):
    name= models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    occupant_count=models.IntegerField(default="")
    admin=models.ForeignKey(neighbourhood,on_delete=models.CASCADE)

    def __str__(self):
        return self.neighbourhood

    def save_neighbourhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood(cls,neighbourhood):
        cls.objects.filter(neighbourhood=neighbourhood).delete()

class user(models.Model):
    name=models.CharField(max_length=100)
    id=models.IntegerField(default='')
    email=models.EmailField()
    neighbourhood_ID = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)


class notifications(models.Model):
    title = models.CharField(max_length=100)
    notification = HTMLField()
    priority = models.CharField(max_length=15,choices=Priority,default="Informational")
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood_ID = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class healthservices(models.Model):
    healthservices = models.CharField(max_length=100)

    def __str__(self):
        return self.healthservices

    def save_healthservices(self):
        self.save()

    @classmethod
    def delete_healthservices(cls,healthservices):
        cls.objects.filter(healthservices=healthservices).delete()


class Business(models.Model):
    logo = models.ImageField(upload_to='businesslogo/')
    description = HTMLField()
    neighbourhood_ID = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    address =models.CharField(max_length=100)
    contact = models.IntegerField()

    def __str__(self):
        return self.name

class Health(models.Model):
    logo = models.ImageField(upload_to='healthlogo/')
    neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address =models.CharField(max_length=100)
    healthservices = models.ManyToManyField(healthservices)

    def __str__(self):
        return self.name

class Authorities(models.Model):
    neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address =models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatars/')
    description = HTMLField()
    neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='post/')
    post = HTMLField()
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood= models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to='avatars/')

    def __str__(self):
        return self.title

    @classmethod
    def search_blog(cls,search_term):
        blogs = cls.objects.filter(Q(username__username=search_term) | Q(neighbourhood__neighbourhood=search_term) | Q(title__icontains=search_term))
        return blogs


class Comment(models.Model):
    comment = models.CharField(max_length=300)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Blog,on_delete=models.CASCADE)
