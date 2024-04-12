from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def home(request):
    return render(request,'files/index.html')

def about(request):
    return render(request,'files/aboutus.html')


def contact(request):
    return render(request,'files/contact.html')

def search(request):
    return render(request,'files/search.html')

def works(request):
    works = Works.objects.all()
    
    dic = {
        'works':works,
        }
    return render(request,'files/works.html',dic)


def work(request,wk):
    work = Works.objects.get(id=wk)
    return render(request,'files/work.html',{'work':work})

def blog(request):
    posts = Post.objects.all()
    

    dic = {
        'posts':posts,
        }
    return render(request,'files/blogs.html',dic)

def post(request,pk):
    post = Post.objects.get(id=pk)
    
    dic = {
        'post':post,
        }
    return render(request,'files/blog.html',dic)


def searched(request):
    if request.method == 'POST':  # Corrected the case of 'POST'
        searched = request.POST.get('searched')  # Corrected retrieving data from request
        prods = Post.objects.filter(
            Q(title__icontains=searched) |
            Q(tags__icontains=searched) |
            Q(category__name__icontains=searched)
        )
        return render(request, 'files/searched.html', {'searched': searched, 'prods': prods})
    
    else:
        return render(request, 'files/searched.html')


