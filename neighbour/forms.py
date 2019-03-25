from django import forms
from .models import Notifications,Business,Profile,Blog,Comment

class NotificationsForm(forms.ModelForm):
    class Meta:
        model=Notifications
        exclude=['title']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user']

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        exclude=['user','neighbourhood','avatar']

class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        exclude=['owner','neighbourhood']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=['user','post']
