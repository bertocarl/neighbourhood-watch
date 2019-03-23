from django import forms
from .models import notifications,Business,Profile,Blog,Comment

class notificationsForm(forms.ModelForm):
    class Meta:
        model=notifications
        exclude=['author','neighbourhood','post_date']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        exclude=['username','neighbourhood','avatar']

class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        exclude=['owner','neighbourhood']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=['username','post']
