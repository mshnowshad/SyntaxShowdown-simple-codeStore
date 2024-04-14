from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def home(request):
    if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            desc = request.POST.get('desc')
            contact = Contact(name=name, email=email, mobile=mobile, desc=desc)
            contact.save()
    return render(request,'files/index.html')

def about(request):
    counts = CounterSection.objects.all()
    return render(request,'files/aboutus.html',{'counts':counts})


def contact(request):
    if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            desc = request.POST.get('desc')
            contact = Contact(name=name, email=email, subject=mobile, desc=desc)
            contact.save()
            
    return render(request,'files/contact.html')

def search(request):
    return render(request,'files/search.html')

def thanku(request):
    if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            desc = request.POST.get('desc')
            contact = Contact(name=name, email=email, mobile=mobile, desc=desc)
            contact.save()
    return render(request,'files/thanku.html')

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


