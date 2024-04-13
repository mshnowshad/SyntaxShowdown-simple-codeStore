
from django.urls import path
from .views import *


urlpatterns = [
    path('',home,name="home"),
    path('about/',about,name="about"),
    path('blog/',blog,name="blog"),
    path('post/<int:pk>',post,name="post"),
    path('contact/',contact,name="contact"),
    path('search/',search,name="search"),
    path('searched/',searched,name="searched"),
    path('works/',works,name="works"),
    path('work/<int:wk>',work,name="work"),
    
    path('thanku/',thanku,name="thanku"),
    # path('searched/',searched,name="searched"),
    
    


    
    
]
