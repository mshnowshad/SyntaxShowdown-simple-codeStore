
from django.urls import path
from .views import *


urlpatterns = [
    path('',home,name="home"),
    path('about/',about,name="about"),
    path('blog/',blog,name="blog"),
    path('post/<int:pk>',post,name="post"),
    path('contact/',contact,name="contact"),
    path('search/',search,name="search"),
    # path('',home,name="home"),
    


    
    
]
