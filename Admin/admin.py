from django.contrib import admin
from .models import *
from HrPanel .models import *


# Register your models here.

@admin.register(User)
class UserAdmin_register(admin.ModelAdmin):
    list_display=['username','first_name','last_name','email','soft_delete','date_joined','phone','domain','position','usertype',]
    
# @admin.register(Position)
# class UserAdmin_position(admin.ModelAdmin):
#     list_display=['position']

@admin.register(Domain_name)
class UserAdmin_domain(admin.ModelAdmin):
    list_display=['domain_name','created_at']

admin.site.register(Office_meeting)
admin.site.register(Interview_meeting)



    