
from django.urls import path
from .views import *


urlpatterns = [
    path('',home,name="home"),
    path('about/',about,name="about"),
    path('blog/',blog,name="blog"),
    path('post/',post,name="post"),
    # path('',home,name="home"),
    # path('',home,name="home"),
    # path('',home,name="home"),
    


    
    
]
