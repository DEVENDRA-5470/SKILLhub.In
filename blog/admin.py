from django.contrib import admin
from blog.models import Blog,Enroll

# Register your models here.

@admin.register(Blog)
class Blogadmin(admin.ModelAdmin):
    list_display=['id','course_img','course_name','course_des','course_duration','course_price']

@admin.register(Enroll)
class Enrolladmin(admin.ModelAdmin):
    list_display=['id','user','course']
