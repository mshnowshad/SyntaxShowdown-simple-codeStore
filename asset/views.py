from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    return render(request,'files/index.html')

def about(request):
    return render(request,'files/aboutus.html')


def contact(request):
    return render(request,'files/contact.html')

def search(request):
    return render(request,'files/search.html')


def blog(request):
    posts = Post.objects.all()
    

    dic = {
        'posts':posts,
        }
    return render(request,'files/blog.html',dic)

def post(request,pk):
    post = Post.objects.get(id=pk)
    
    dic = {
        'post':post,
        }
    return render(request,'files/bloginner.html',dic)


