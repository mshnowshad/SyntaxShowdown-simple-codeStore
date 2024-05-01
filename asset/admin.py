from turtle import pos
from django.contrib import admin
from .models import Category,Post,CategoryWork,Works,Contact,CounterSection
# Register your models here.



class PostAdmin(admin.ModelAdmin):  #ADMIN PANEL CUSTOMIZED OF PRODUCTLIST
    list_display = ('id','title','upload_in')
    list_display_links = ('id','title')
    search_fields = ('title','category','upload_in')

class WorksAdmin(admin.ModelAdmin):  #ADMIN PANEL CUSTOMIZED OF PRODUCTLIST
    list_display = ('id','title','upload_in')
    list_display_links = ('id','title')
    search_fields = ('title','work_time','tools','upload_in') 


admin.site.register(Category)
admin.site.register(CategoryWork)
admin.site.register(Post,PostAdmin)
admin.site.register(Works,WorksAdmin)
admin.site.register(Contact)
admin.site.register(CounterSection)




