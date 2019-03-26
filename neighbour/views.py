from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Neighbourhood,Business,Blog,Profile,Notifications,Comment
from .email import send_priority_email
from .forms import NotificationsForm,ProfileForm,BlogForm,BusinessForm,CommentForm
from decouple import config,Csv
import datetime as dt
from django.http import JsonResponse
import json
from django.db.models import Q
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import BusinessSerializer



def index(request):
    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        current_user=request.user
        blogs= Blog.objects.all()
        profile= Profile.objects.all()
        comments= Comment.objects.all()
        business= Business.objects.all()
        all_notifications= Notifications.objects.all()
        
        
    except ObjectDoesNotExist:
        return redirect('create-profile')

    return render(request,'index.html')

@login_required(login_url='/accounts/login/')
def notification(request):
    current_user = request.user
    all_notifications = Notifications.objects.filter()

    return render(request,'notifications.html',{"all_notifications":all_notifications})

@login_required(login_url='/accounts/login/')
def blog(request):
    current_user = request.user
    blogs = Blog.objects.filter()

    return render(request,'blog.html',{"blogs":blogs})

@login_required(login_url='/accounts/login/')


@login_required(login_url='/accounts/login/')
def businesses(request):
    current_user=request.user
    businesses = Business.objects.filter()

    return render(request,'businesses.html',{"businesses":businesses})

@login_required(login_url='/accounts/login/')
def view_blog(request,id):
    current_user = request.user

    try:
        comments = Comment.objects.filter(post_id=id)
    except:
        comments =[]

    blog = Blog.objects.get(id=id)
    if request.method =='POST':
        form = CommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.post = blog
            comment.save()
    else:
        form = CommentForm()

    return render(request,'view_blog.html',{"blog":blog,"form":form,"comments":comments})

@login_required(login_url='/accounts/login/')
def my_profile(request):
    current_user=request.user
    profile =  Profile.objects.filter()
    
    return render(request,'user_profile.html',{"profile":profile})


@login_required(login_url='/accounts/login/')
def user_profile(request,user):
    user = User.objects.get(user=user)
    profile = Profile.objects.filter()
   
    return render(request,'user_profile.html',{"profile":profile})

@login_required(login_url='/accounts/login/')
def new_blog(request):
    user=request.user
    if request.method=="POST":
        form =BlogForm(request.POST,request.FILES)
        if form.is_valid():
            blog = form.save(commit = False)
            blog.user = current_user
            blog.neighbourhood = profile.neighbourhood
            blog.avatar = profile.avatar
            blog.save()

        return redirect('blog')

    else:
        form = BlogForm()
    context = {
      'form': form
   }

    return render(request,'blog_form.html', context)

@login_required(login_url='/accounts/login/')
def new_business(request):
    current_user=request.user
    
    if request.method=="POST":
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            business = form.save(commit = False)
            business.owner = current_user
            business.neighbourhood = profile.neighbourhood
            business.save()

        return HttpResponseRedirect('/businesses')

    else:
        form = BusinessForm()

    return render(request,'business_form.html',{"form":form})


@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user=request.user
    if request.method=="POST":
        form =ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:

        form = ProfileForm()
    return render(request,'profile_form.html',{"form":form})

@login_required(login_url='/accounts/login/')
def new_notification(request):
    current_user=request.user
   

    if request.method=="POST":
        form = NotificationsForm(request.POST,request.FILES)
        if form.is_valid():
            notification = form.save(commit = False)
            notification.author = current_user
            notification.hood = Profile.Neighbourhood
            notification.save()

            if notification.priority == 'High Priority':
                send_priority_email(profile.name,profile.email,notification.title,notification.notification,notification.author,notification.neighbourhood)

        return HttpResponseRedirect('/notifications')


    else:
        form = NotificationsForm()

    return render(request,'notifications_form.html',{"form":form})

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user=request.user
    if request.method=="POST":
        instance = Profile.objects.get(user=current_user)
        form =ProfileForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.user = current_user
            profile.save()

        return redirect('Index')

    elif Profile.objects.get(user=current_user):
       
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm()

    return render(request,'update_profile.html',{"form":form})



@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_business = Business.search_business(search_term)
        message=f"{search_term}"

        print(searched_business)

        return render(request,'search.html',{"message":message,"searched_business":searched_business})

    else:
        message="You haven't searched for any term"
        return render(request,'search.html',{"message":message})

class BusinessList(APIView):
    def get(self, request, format=None):
        all_business = Business.objects.all()
        serializers = BusinessSerializer(all_business, many=True)
        return Response(serializers.data)

