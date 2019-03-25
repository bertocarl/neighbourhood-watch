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

    @classmethod
    def search_business(cls,search_term):
        businesses = cls.objects.filter(Q(user__user=search_term) | Q(hood__hood=search_term) | Q(owner__owner=search_term) | Q(address__address=search_term) | Q(title__icontains=search_term))
                
        return businesses

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

    


class Comment(models.Model):
    comment = models.CharField(max_length=300)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Blog,on_delete=models.CASCADE)
