from django.contrib import admin
from django.urls import path
from Admin  import views


urlpatterns = [
    path('',views.admindashboard),
    
    path('create_newuser/',views.create_newuser, name='create_newuser'),
    path('updatedetete/<id>/<data>',views.update_user , name='updatedetete'),
        
    path('domain/',views.Useraddshoedomains.as_view() , name='domain'),
    path('domainupdatedelete/<id>/<data>/',views.updatedesignation, name='domainupdatedelete'),

    path('admin_add_interview/', views.admin_create_interview, name="admin_add_interview"),
    path('admin_editdelete_interview/<id>/<data>', views.admin_edit_interview, name="admin_editdelete_interview"),
    path('admin_intreview_details/<data>',views.Interview_meetings , name='admin_intreview_details'),
   
    
    path('admin_create_offcemeeting',views.admin_create_offcemeeting, name='admin_create_offcemeeting'),
    path('admin_editdelete_officemeet/<id>/<data>/', views.admin_edit_officemeet,name='admin_editdelete_officemeet'),
    path('admin_officemeeting/<data>',views.office_meetings , name='admin_officemeeting'),
   
]
