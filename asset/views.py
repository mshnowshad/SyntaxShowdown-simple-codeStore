from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'files/index.html')

def about(request):
    return render(request,'files/aboutus.html')




def blog(request):
    return render(request,'files/blog.html')

def post(request):
    return render(request,'files/bloginner.html')


