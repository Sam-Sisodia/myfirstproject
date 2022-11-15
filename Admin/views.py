from datetime import datetime
from lib2to3.pgen2 import token
from tkinter.messagebox import NO
from django.shortcuts import render,redirect, HttpResponse,HttpResponseRedirect
from django.contrib.auth import logout as user_logout
from .models import  *
from . email import *
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as user_logout
from HrPanel.models import *
from django.contrib.auth.decorators import login_required
from .form import *
import uuid

# def emp_count():
#     emp_code =0
#     emp_user = User.objects.all().count()
#     if emp_user:
#         return emp_user
#     else:
#         return emp_code

def create_newuser(request):
    obj_desiganations = Domain_name.objects.all()
    form = UserRegistarionForm(request.POST)
    if  request.method == "POST":
        if form.is_valid():
            obj =form.save()
            send_login_email(obj.email)
            obj.set_password(user_pass)
            
            obj.save()
            return  redirect("/adminpanel")

        else:
            not_add=True

    return render(request ,"adminadduser.html",locals())

def admindashboard(request):
    users = User.objects.filter(soft_delete=False)
    context = {'users':users}
    return render(request,'admindashboard.html', context )


def update_user(request, id, data=None):
    obj = User.objects.get(id=id)
    form = UserRegistarionForm(request.POST)
    obj_desiganations = Domain_name.objects.all()
    if request.method == "POST":
        if data =="edit":
            username= request.POST.get("username")
            email = request.POST.get("email")
            address = request.POST.get("address")
            phone_no = request.POST.get("phone")
            domain = request.POST.get("domain")
            position = request.POST.get("position")
            usertype = request.POST.get("usertype")
            obj.username = username
            obj.email = email
            obj.phone = phone_no
            obj.address = address
            objs = Domain_name.objects.get(id=domain)
            obj.domain = objs
        
            obj.position = position
            obj.usertype = usertype
            obj.save()
        
            return  redirect("/adminpanel")

    elif data == "delete":   
        obj.soft_delete = True
        obj.save()
        return redirect('/adminpanel')

    return render(request , "edituserdetails.html",locals())

from django.views.generic.base import TemplateView,RedirectView

class Useraddshoedomains(TemplateView):
    template_name = 'domain.html'

    def get_context_data(self,*args, **kwargs):
        context= super().get_context_data(**kwargs)
        fm = Desiganationform()
        domain_names = Domain_name.objects.filter(soft_delete=False)
        context = {'fm':fm,'domain_names':domain_names}
        return  context

    def post(self,request):
        domain_names = Domain_name.objects.filter(soft_delete=False)
        fm = Desiganationform(request.POST)

        if fm.is_valid():
           fm.save()
        else:
            fm = Desiganationform(request.POST)

            context = {'fm':fm}           
        return render(request ,'domain.html',locals())



def updatedesignation(request, id, data=None):
    domain_names = Domain_name.objects.filter(soft_delete=False)
    obj = Domain_name.objects.get(id=id)
    if request.method == "POST":
            if data =="edit":
                obj.domain_name= request.POST.get("domain_name")
                obj.save()
                return redirect('domain')

    elif data == "delete":   
        obj.soft_delete= True
        obj.save()
        return redirect('domain')
        
    return  render (request, 'domain.html',locals())



'''


def updatedesignation(request, id, data=None):
    domain_names = Domain_name.objects.filter(soft_delete=False)
    obj = Domain_name.objects.get(id=id)
    if request.method == "POST":
    
            obj.domain_name= request.POST.get("domain_name")
            obj.save()
            return redirect('domain')

    elif data == "delete":   
        print("OBJ IS ====== ",obj)
        obj.soft_delete= True
        
        obj.delete()
        return redirect('domain')
    
'''






def admin_create_interview(request):
    obj_desiganations = Domain_name.objects.filter(soft_delete=False)
    iform = interviewform(request.POST)
    form = UserRegistarionForm(request.POST)
    users = User.objects.filter(soft_delete=False)
    if  request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        cv = request.FILES['cv']
        domain = request.POST.get("domain")
        position = request.POST.get("position")
        status = request.POST.get("status")

        email = request.POST.get("email")
        phone = request.POST.get("phone")
        datetime = request.POST.get("datetime")
        users = request.POST.getlist('userlist')

        obj = Interview_meeting.objects.create(first_name = fname, last_name = lname, email = email , user_cv = cv, phone =phone, datetime= datetime,
                    domain_id= domain , status=status, position=position)
        for user in users:
            obj.user.add(User.objects.get(id=user))
        return redirect('/adminpanel/admin_intreview_details/all')

    else:
        form = UserRegistarionForm(request.POST)
        usrrlist = request.POST.getlist('userlist')
       
    return  render(request, "admin_createinterview.html",locals())




from datetime import datetime, timedelta
from django.views  import View

from django.utils import timezone

def Interview_meetings(request, data=None):
    now = datetime.now() 
    new =  datetime.now() + timedelta(days=1) 
    if data == "all":
        intreview_obj = Interview_meeting.objects.filter(soft_delete=False)
    if data =="today":
        intreview_obj = Interview_meeting.objects.filter(datetime__range =  [datetime.today(),now+timedelta(days=1)],soft_delete = False)
       
    if data =="upcoming":
        intreview_obj = Interview_meeting.objects.filter(datetime__range =[datetime.today(),now+timedelta(days=3)],soft_delete = False) 
    
    if data =="past":
        intreview_obj = Interview_meeting.objects.filter(datetime__lt =now) 

    return  render(request,'admin_intreview_details.html',{'intreview_obj':intreview_obj})



def admin_edit_interview(request,id,data=None):
    iobj =  Interview_meeting.objects.get(id=id)
    obj_desiganations = Domain_name.objects.all()
    iform = interviewform(request.POST)
    form = UserRegistarionForm(request.POST)
    users = User.objects.filter(soft_delete=False)
   
    if request.method =="POST":
        if data == "edit":
            pass

    elif data == "delete":
        iobj.soft_delete = True
        iobj.save()
        return  redirect("/adminpanel/admin_intreview_details/all")


    return render(request,'admin_edit_interview.html',locals())










#office Meeting


def office_meetings(request,data=None): 
    now = datetime.now() 
    new =  datetime.now() + timedelta(days=1)
    if data == "all":
        meetings  = Office_meeting.objects.filter(soft_delete = False)
        

    if data == "today":
        meetings = Office_meeting.objects.filter(datetime__range =  [datetime.today(),now+timedelta(days=1)],soft_delete = False)
    
    if data =="upcoming":
        meetings = Office_meeting.objects.filter(datetime__range =[datetime.today(),now+timedelta(days=3)],soft_delete = False) 

    if data =="past":
        meetings = Office_meeting.objects.filter(datetime__lt =now) 

    return render(request,'aofficemeet.html',{'meetings':meetings}) 

def admin_create_offcemeeting(request):
    users = User.objects.all()
    if request.method=="POST":
        agenda = request.POST.get('agenda')
        discription = request.POST.get('discription')
        users = request.POST.getlist('user')
        datetime= request.POST.get('datetime')
        meet=Office_meeting.objects.create(Meeting_Agenda=agenda,Description=discription,datetime=datetime)
        for user in users:
            meet.user.add(User.objects.get(id=user))
        return redirect('/adminpanel/admin_officemeeting/all')

    return render(request,'admin_officemeet.html',locals())



def admin_edit_officemeet(request,id,data=None):
    users = User.objects.all()
    objs =  Office_meeting.objects.get(id=id)
    print(objs.soft_delete)
    
    if request.method=="POST":
        if data =="edit":
            agenda = request.POST.get('agenda')
            discription = request.POST.get('discription')
            datetime= request.POST.get('datetime')
            users = request.POST.getlist('user')

            objs.Meeting_Agenda= agenda
            objs.Description = discription
            objs.datetime  = datetime

            objs.save()
            for user in users:
                objs.user.add(User.objects.get(id=user))
            return redirect('admin_officemeeting')

    elif data == "delete":   
        objs.soft_delete = True
        objs.save()
        return  redirect("/adminpanel/admin_officemeeting/all")

    return render(request,'admin_edit_officemeet.html',locals())


def login(request):
    if  request.method == "POST":
        username = request.POST.get('name')
        password =request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)

        if user is not None:
            auth_login(request, user)
            user=request.user
            if user.usertype =="HR":
                return render(request, 'adminadduser.html')

            if user.usertype =="Admin" or user.usertype =="MD":
                return redirect('http://127.0.0.1:8000/adminpanel/')
            

             # return HttpResponse("User register ")
        else:
            #return HttpResponse("User Not ragister ")
            messages.info(request ,"Incorrect Username or Password")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def logout(request):
    user_logout(request)
    return redirect('/login')



import uuid
def forgetpassword(request):
    current_user= request.user
    try:
        if request.method == "POST":
            username= request.POST.get('username')
            if not User.objects.filter(username=username).first():
                messages.success(request, "No User Found with this Username")
                return render(request, 'forgetpass.html')

            user_obj = User.objects.get(username=username)
            token=  str(uuid.uuid4())
            profile_obj = Profile.objects.create(user=user_obj,forget_password_token = token)
        

            send_forgetpassword_email(user_obj.email,token)
            messages.success(request, "An email Send your mail please check Your Mail")
            return render(request, 'forgetpass.html')


    

    except Exception as e:
        print(e)

    return render(request, 'forgetpass.html')

def delete_token(request, id):
#     token  = Profile.objects.get(user_id=id)
#     token.delete()
     return redirect('/login')

def resetpassword(request,token):
    context= {}
    
    try:
        profile_obj = Profile.objects.get(forget_password_token=token)
        context= {'user_id': profile_obj.user.id}

        if request.method=="POST":
            new_password=request.POST.get('new_password')
            confirm_password=request.POST.get('confirm_password')
            user_id = request.POST.get('user_id')
        
            if user_id is None:
                messages.success(request, f"User Id  Not Found")
                return redirect(f'/resetpassword/{token}/')

            if new_password != confirm_password:
                messages.success(request, "Password not match")
                return redirect(f'/resetpassword/{token}/')

            user_obj = User.objects.get(id=user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            token=Profile.objects.get(user=user_id)
            token.delete()
          

            messages.success(request, "Password Chage Successdully ")

            return redirect('login')
            

    except Exception as e:
        print(e)
    return render(request, 'resetpassword.html', context)


    




