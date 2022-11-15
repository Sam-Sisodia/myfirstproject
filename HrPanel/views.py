# from django.shortcuts import render,redirect
# from .models import Interview_meeting
# from .models import Office_meeting
# from .forms import Interview_meeting_Form,Office_meeting_Form
# from Admin.models import *
# from django.core.exceptions import ValidationError
# import datetime
# from django.core.files.storage import FileSystemStorage
# from django.contrib import messages


# # Create your views here.
# def Interview(request):
#     domains=Domain_name.objects.all()
# <<<<<<< HEAD
#     positions=positon
#     # print(domains)
#     # for i in domains:
#     #     print(i.id,i.domain_name,'karan')
         
# =======
#     positions=Position.objects.all()
# >>>>>>> ed708f8305f95cb61e6dc5ec138ad73ad574dc8a
#     form=Interview_meeting_Form()
#     data=Interview_meeting.objects.filter(soft_delete='False')
#     user=User.objects.all()
#     # datausers={}
#     # for i in data:
#     #     datausers[i.id]=[j.username for j in i.user.all()]  
#     if request.method=='POST':
#         form=Interview_meeting_Form(request.POST,request.FILES)
#         print("vishal")
#         if form.is_valid():
# <<<<<<< HEAD
# =======
#             print("karan")
# >>>>>>> ed708f8305f95cb61e6dc5ec138ad73ad574dc8a
#             # first_name=form.cleaned_data['first_name']
#             # last_name=form.cleaned_data['last_name']
#             # email=form.cleaned_data['email']
#             # user_cv=request.FILES['user_cv']
#             # phone=form.cleaned_data['phone']
#             # datetime=form.cleaned_data['datetime']
#             # domain=form.cleaned_data['domain']
#             # position=form.cleaned_data['position']
#             # user_list=form.cleaned_data['user']
            
#             # data=form.save()
#             # print(data.position)
#             # data.user="jjh"
#             # data.save()
            
#             # interview=Interview_meeting.objects.create(first_name=first_name,last_name=last_name,email=email,user_cv=user_cv,phone=phone,datetime=datetime,position=position,domain=domain)
# <<<<<<< HEAD
#             # interview=form.save()
#             form.save()
#             # for i in user:
#             #     interview.user.add(i.id)
#             #     interview.save()
# =======
#             interview=form.save()
#             for i in user:
                
#                 interview.user.add(i.id)
#                 interview.save()
# >>>>>>> ed708f8305f95cb61e6dc5ec138ad73ad574dc8a
#             messages.success(request, 'interview sheduled successfull')
#     return render(request,'interviewhr.html',locals())


# def Interviewdelete(request,id):
#     Interview_meeting.objects.filter(id=id).update(soft_delete=True)
#     return redirect('interviewdata')

# def Interviewupdate(request,id):
#     domains=Domain_name.objects.all()
#     # positions=Position.objects.all()
#     value=Interview_meeting.objects.get(id=id)
# <<<<<<< HEAD
#     form=Interview_meeting_Form(instance=value)
# =======
#     print(value.domain,'karan')
# >>>>>>> ed708f8305f95cb61e6dc5ec138ad73ad574dc8a
#     many_users=value.user.values_list("id")  
#     updating = True
#     user_id=[]
#     for i in many_users:
#         for j in i:
#             user_id.append(j)
    
#     data=Interview_meeting.objects.filter(soft_delete='False')
#     user=User.objects.filter(soft_delete='False',domain=value.domain)
#     unadduser_id=[]
#     for i in user:
#         if i.id not in user_id:
#               unadduser_id.append(i.id)
#     datausers={}
#     for i in data:
#         datausers[i.id]=[j.username for j in i.user.all()]  
        
# <<<<<<< HEAD
# =======
#     print(datausers)
# >>>>>>> ed708f8305f95cb61e6dc5ec138ad73ad574dc8a
#     if request.method=='POST':
#         form=Interview_meeting_Form(request.POST)
#         if form.is_valid():
#             first_name=form.cleaned_data['first_name']
#             last_name=form.cleaned_data['last_name']
#             email=form.cleaned_data['email']
           
#             phone=form.cleaned_data['phone']
#             datetime=form.cleaned_data['datetime']
#             user_list=form.cleaned_data['user']
#             domain=form.cleaned_data['domain']
#             position=form.cleaned_data['position']
            
#             interview = Interview_meeting.objects.get(id=id)
#             interview.first_name=first_name
#             interview.last_name =last_name
#             interview.email=email
#             interview.phone=phone
#             interview.datetime=datetime
#             interview.position=position
#             interview.domain=domain

            
#             # interview=Interview_meeting(id=id,first_name=first_name,last_name=last_name,email=email,phone=phone,datetime=datetime,position=position,domain=domain)
#             if request.FILES.get('user_cv'):
#                 interview.user_cv=request.FILES['user_cv']   
#             interview.save()
                
#             for i in user_list:
#                 interview.user.add(i.id)
#                 interview.save()
#             return redirect('interviewdata')
            
            
   
   
#     return render(request,'interviewhr.html',locals())

    


# def Office_meetings(request):
#     data=Office_meeting.objects.filter(soft_delete='False')
#     user=User.objects.all()
#     datausers={}
#     for i in data:
#         datausers[i.id]=[j.username for j in i.user.all()]  
#     if request.method=='POST':
#         form=Office_meeting_Form(request.POST)
#         if form.is_valid():
#             # Meeting_Agenda=form.cleaned_data['Meeting_Agenda']
#             # Description=form.cleaned_data['Description']
#             # datetime=form.cleaned_data['datetime']
#             # user_list=form.cleaned_data['user']
#             # print(Meeting_Agenda,Description,datetime,user_list)
#             # office_meeting=Office_meeting.objects.create(Meeting_Agenda=Meeting_Agenda,Description=Description,datetime=datetime)
# <<<<<<< HEAD
#             # office_meeting=form.save()
#             form.save()
#             # for i in usert:
#             #     office_meeting.user.add(i.id)
#             #     office_meeting.save()
# =======
#             office_meeting=form.save()
#             for i in user_list:
#                 office_meeting.user.add(i.id)
#                 office_meeting.save()
# >>>>>>> ed708f8305f95cb61e6dc5ec138ad73ad574dc8a
#             messages.success(request, 'Office meeting sheduled successfull')
#     return render(request, 'office_meetings.html',locals())

# def Office_meetingsdelete(request,id):
#     Office_meeting.objects.filter(id=id).update(soft_delete=True)
#     return redirect('office_meetingdata')

# def Office_meetingsupdate(request,id):
#     value=Office_meeting.objects.get(id=id)
#     data=Office_meeting.objects.filter(soft_delete='False')
#     many_users=value.user.values_list("id")  
#     user_id=[]
#     for i in many_users:
#         for j in i:
#             user_id.append(j)
    
#     data=Interview_meeting.objects.filter(soft_delete='False')
#     user=User.objects.filter(soft_delete='False')
#     unadduser_id=[]
#     for i in user:
#         if i.id not in user_id:
#               unadduser_id.append(i.id)
#     datausers={}
#     for i in data:
#         datausers[i.id]=[j.username for j in i.user.all()]  
#     if request.method=='POST':
#         form=Office_meeting_Form(request.POST)
#         if form.is_valid():
#             Meeting_Agenda=form.cleaned_data['Meeting_Agenda']
#             Description=form.cleaned_data['Description']
#             datetime=form.cleaned_data['datetime']
#             user_list=form.cleaned_data['user']
#             office_meeting=Office_meeting(id=id,Meeting_Agenda=Meeting_Agenda,Description=Description,datetime=datetime)
#             for i in user_list:
#                 office_meeting.user.add(i.id)
#                 office_meeting.save()
#             return redirect('office_meetingdata')
    
#     return render(request, 'office_meetings.html',locals())

# def interviewdata(request):
#     todaydate=datetime.datetime.today()
#     todaydata=Interview_meeting.objects.filter(datetime__year=todaydate.year,datetime__month=todaydate.month,datetime__day=todaydate.day,datetime__hour__gte=todaydate.hour,soft_delete=False)
#     data=Interview_meeting.objects.filter(soft_delete='False')
#     user=User.objects.all()
#     datausers={}
#     for i in data:
#         datausers[i.id]=[j.username for j in i.user.all()]  
#     return render(request, 'interviewdata.html',locals())
    
# def office_meetingdata(request):
#     todaydate=datetime.datetime.today()
#     todaydata=Office_meeting.objects.filter(datetime__year=todaydate.year,datetime__month=todaydate.month,datetime__day=todaydate.day,datetime__hour__gte=todaydate.hour,soft_delete=False)
#     data=Office_meeting.objects.filter(soft_delete='False')
#     user=User.objects.all()
#     datausers={}
#     for i in data:
#         datausers[i.id]=[j.username for j in i.user.all()]  
#     return render(request, 'office_meetingdata.html',locals())


# def user_data(request):
#     programing_id=request.GET.get('programming')
#     # position=Position.objects.filter(position='sr.')
#     # print(position)
# <<<<<<< HEAD
#     user=User.objects.filter(domain=programing_id,position='Sr')
# =======
#     user=User.objects.filter(domain=programing_id)
# >>>>>>> ed708f8305f95cb61e6dc5ec138ad73ad574dc8a
#     # datausers={}
#     # for i in data:
#     #     datausers[i.id]=[j.username for j in i.user.all()]
#     return render(request, 'userajax.html',{"user":user})

# def showhrdashboard(request):
# <<<<<<< HEAD
#     form=Interview_meeting_Form()
#     total=Interview_meeting.objects.filter(soft_delete='False')
# =======
#     total=Interview_meeting.objects.filter(status="Hold",soft_delete='False')
# >>>>>>> ed708f8305f95cb61e6dc5ec138ad73ad574dc8a
#     accepted=Interview_meeting.objects.filter(status="Selected",soft_delete='False')
#     rejected=Interview_meeting.objects.filter(status="Rejected",soft_delete='False')
#     data_total=total.count()
#     data_accepted=accepted.count()
#     data_rejected=rejected.count()
# <<<<<<< HEAD
#     data=Interview_meeting.objects.filter(soft_delete='False',status="Hold")
#     user=User.objects.all()
#     datausers={}
#     for i in data:
#         datausers[i.id]=[j.username for j in i.user.all()] 
# =======
# >>>>>>> ed708f8305f95cb61e6dc5ec138ad73ad574dc8a

    
#     return render(request, 'showhrdashboard.html',locals())

# <<<<<<< HEAD
# def status(request,id):
#     if request.method=='POST':
#         status=request.POST['status']
#         Interview_meeting.objects.filter(id=id).update(status=status)
   
#     return redirect('showhrdashboard')

# =======
# >>>>>>> ed708f8305f95cb61e6dc5ec138ad73ad574dc8a
