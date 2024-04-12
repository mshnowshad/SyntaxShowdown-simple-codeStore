from turtle import pos
from django.contrib import admin
from .models import Category,Post,CategoryWork,Works
# Register your models here.


admin.site.register(Category)
admin.site.register(CategoryWork)
admin.site.register(Post)
admin.site.register(Works)


