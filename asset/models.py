from email.policy import default
from django.db import models

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'

class Post(models.Model):
    title = models.CharField(max_length=3000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Removed default value
    image = models.ImageField(upload_to='uploads/post/', blank=False, null=False)
    check_1 = models.BooleanField(default=True)
    step_1 = models.TextField(default='', blank=False, null=False)
    code_1 = models.TextField(default='', blank=False, null=False)
    check_2 = models.BooleanField(default=False)
    image_2 = models.ImageField(upload_to='uploads/post/', blank=True, null=True)
    step_2 = models.TextField(default='', blank=True, null=True)
    code_2 = models.TextField(default='', blank=True, null=True)
    check_3 = models.BooleanField(default=False)
    image_3 = models.ImageField(upload_to='uploads/post/', blank=True, null=True)
    step_3 = models.TextField(default='', blank=True, null=True)
    code_3 = models.TextField(default='', blank=True, null=True)
    check_4 = models.BooleanField(default=False)
    image_4 = models.ImageField(upload_to='uploads/post/', blank=True, null=True)
    step_4 = models.TextField(default='', blank=True, null=True)
    code_4 = models.TextField(default='', blank=True, null=True)
    check_5 = models.BooleanField(default=False)
    image_5 = models.ImageField(upload_to='uploads/post/', blank=True, null=True)
    step_5 = models.TextField(default='', blank=True, null=True)
    code_5 = models.TextField(default='', blank=True, null=True)
    check_6 = models.BooleanField(default=False)
    image_6 = models.ImageField(upload_to='uploads/post/', blank=True, null=True)
    step_6 = models.TextField(default='', blank=True, null=True)
    code_6 = models.TextField(default='', blank=True, null=True)
    check_7 = models.BooleanField(default=False)
    image_7 = models.ImageField(upload_to='uploads/post/', blank=True, null=True)
    step_7 = models.TextField(default='', blank=True, null=True)
    code_7 = models.TextField(default='', blank=True, null=True)
    check_8 = models.BooleanField(default=False)
    image_8 = models.ImageField(upload_to='uploads/post/', blank=True, null=True)
    step_8 = models.TextField(default='', blank=True, null=True)
    code_8 = models.TextField(default='', blank=True, null=True)
    check_9 = models.BooleanField(default=False)
    image_9 = models.ImageField(upload_to='uploads/post/', blank=True, null=True)
    step_9 = models.TextField(default='', blank=True, null=True)
    code_9 = models.TextField(default='', blank=True, null=True)
    tags = models.TextField(default='', blank=True, null=True)
    source_code = models.URLField(max_length=10000, blank=True, null=True) #<----এটি মানে হল ফিল্ডটি ফর্মে একটি মান প্রবেশ করার জন্য বাধ্যতা নেই। অর্থাৎ, ফিল্ডটি খালি অথবা মান না দিয়েও ফর্ম সাবমিট করা যাবে।
    upload_in = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-upload_in',)
    
    def __str__(self):
        return self.title
   
class CategoryWork(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'category_works'


class Works(models.Model):
    title = models.CharField(max_length=30000)
    work_time = models.CharField(max_length=3000,default="",blank=True, null=True)
    category = models.ForeignKey(CategoryWork, on_delete=models.CASCADE)  # Removed default value
    image0 = models.ImageField(upload_to='uploads/works/', blank=True, null=True)
    image1 = models.ImageField(upload_to='uploads/works/', blank=True, null=True)
    image2 = models.ImageField(upload_to='uploads/works/', blank=True, null=True)
    image3 = models.ImageField(upload_to='uploads/works/', blank=True, null=True)
    image4 = models.ImageField(upload_to='uploads/works/', blank=True, null=True)
    image5 = models.ImageField(upload_to='uploads/works/', blank=True, null=True)
    description = models.TextField(default='', blank=True, null=True)
    tools = models.TextField(default='', blank=True, null=True)
    web_link = models.URLField(max_length=10000, blank=True, null=True)
    source_code = models.URLField(max_length=10000, blank=True, null=True) #<----এটি মানে হল ফিল্ডটি ফর্মে একটি মান প্রবেশ করার জন্য বাধ্যতা নেই। অর্থাৎ, ফিল্ডটি খালি অথবা মান না দিয়েও ফর্ম সাবমিট করা যাবে।
    upload_in = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-upload_in',)
        verbose_name_plural = 'Works'
    
    def __str__(self):
        return self.title




class Contact(models.Model): 
    id = models.AutoField(primary_key=True, default=None) 
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    mobile = models.CharField(max_length=30, blank=True, null=True)
    desc = models.TextField()
    
    
    def __str__(self):
        return self.name
    
    
    



    





