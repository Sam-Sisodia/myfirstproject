# from django import forms
# import re
# from .models import Interview_meeting,Office_meeting
# from django.core.exceptions import ValidationError

# class Interview_meeting_Form(forms.ModelForm):
#     class Meta:
#         model=Interview_meeting
#         fields=('first_name','last_name','email','datetime','user_cv','phone','user','domain','position','status')
        
# <<<<<<< HEAD
#     def __init__(self, *args, **kwargs):
# =======
#     def __init__(self, args, *kwargs):
# >>>>>>> ed708f8305f95cb61e6dc5ec138ad73ad574dc8a
#         super().__init__(*args, **kwargs)
#         self.fields['position'].widget.attrs.update({"class": "form-select"})
        
        
#     def clean_first_name(self):
#         first_name = self.cleaned_data["first_name"]
#         if first_name == "":
#             raise forms.ValidationError("This field is required. ")
#         elif  first_name.isalpha() == False:
#             raise forms.ValidationError("Enter only letter")
#         return first_name
    
#     def clean_last_name(self):
#         last_name = self.cleaned_data["last_name"]
#         if last_name == "":
#             raise forms.ValidationError("This field is required. ")
#         elif  last_name.isalpha() == False:
#             raise forms.ValidationError("Enter only letter")
#         return last_name
    
#     def clean_datetime(self):
#         datetime = self.cleaned_data["datetime"]
#         if datetime == "":
#             raise forms.ValidationError("This field is required. ")
#         return datetime
    
#     # def clean_user_cv(self):
#     #     user_cv = self.cleaned_data["user_cv"]
#     #     if user_cv == "":
#     #         raise forms.ValidationError("This field is required. ")
#     #     return user_cv
    
    
#     def clean_email(self):
#         email = self.cleaned_data["email"]
#         if email == "":
#             raise forms.ValidationError("This field is required. ")
#         return email


#     def clean_phone(self):
#         phone = self.cleaned_data["phone"]
#         # Pattern = re.compile("[7-9][0-9]{9}")
#         # if Pattern.match(phone)
#  :
#         #     raise forms.ValidationError("Invalid Mobile Number")
#         if len(str(phone)) > 10 or len(str(phone)) < 10:
#             raise forms.ValidationError("Number is not valid (Enter a 10 digit number)")
#         return phone
    
    
#     def clean_datetime(self):
#         datetime = self.cleaned_data['datetime']
#         todaydate=datetime.today()
#         if  datetime.year < todaydate.year :
#             raise forms.ValidationError("give the correct present date not past date ")
#         elif  datetime.month < todaydate.month :
#             raise forms.ValidationError("give the correct present date not past date ")
#         elif  datetime.month == todaydate.month :
#             if datetime.day < todaydate.day:
#                 raise forms.ValidationError("give the correct present date not past date ")
#             elif datetime.day == todaydate.day:
#                 if datetime.hour <= todaydate.hour:
#                     raise forms.ValidationError("give the correct present date not past date ")
#         if Interview_meeting.objects.filter(datetime__year=datetime.year,datetime__month=datetime.month,datetime__day=datetime.day,datetime__hour=datetime.hour,soft_delete=False).exists():
#             raise forms.ValidationError(f"this date time is already taken please extend 1 hour to this time {datetime.hour}:00") 
#         elif datetime.minute != 00:
#             raise forms.ValidationError("please minute should be 00 .")                         
#         return datetime  
    
#     def clean_user(self):
#         user = self.cleaned_data["user"]
#         if user == "":
#             raise forms.ValidationError("This field is required. ")
#         return user 
    
#     # def clean_domain(self):
#     #     domain = self.cleaned_data["domain"]
#     #     if domain == "":
#     #         raise forms.ValidationError("This field is required. ")
#     #     return domain
    
#     # def clean_position(self):
#     #     position = self.cleaned_data["position"]
#     #     if position == "":
#     #         raise forms.ValidationError("This field is required. ")
#     #     return position   
    
    
    
# class Office_meeting_Form(forms.ModelForm):
#     class Meta:
#         model=Office_meeting
#         fields=('Meeting_Agenda','Description','datetime','user')
        
#     def clean_Meeting_Agenda(self):
#         Meeting_Agenda = self.cleaned_data["Meeting_Agenda"]
#         if Meeting_Agenda == "":
#             raise forms.ValidationError("This field is required. ")
#         # elif  Meeting_Agenda.isalpha() == False:
#         #     raise forms.ValidationError("Enter only letter")
#         return Meeting_Agenda
    
#     def clean_Description(self):
#         Description = self.cleaned_data["Description"]
#         if Description == "":
#             raise forms.ValidationError("This field is required. ")
#         return Description
    
#     def clean_datetime(self):
#         datetime = self.cleaned_data['datetime']
#         todaydate=datetime.today()
#         if  datetime.year < todaydate.year :
#             raise forms.ValidationError("give the correct present date not past date ")
#         elif  datetime.month < todaydate.month :
#             raise forms.ValidationError("give the correct present date not past date ")
#         elif  datetime.month == todaydate.month :
#             if datetime.day < todaydate.day:
#                 raise forms.ValidationError("give the correct present date not past date ")
#             elif datetime.day == todaydate.day:
#                 if datetime.hour <= todaydate.hour:
#                     raise forms.ValidationError("give the correct present date not past date ")
#         if Office_meeting.objects.filter(datetime__year=datetime.year,datetime__month=datetime.month,datetime__day=datetime.day,datetime__hour=datetime.hour,soft_delete=False).exists():
#             raise forms.ValidationError(f"this date time is already taken please extend 1 hour to this time {datetime.hour}:00") 
#         elif datetime.minute != 00:
#             raise forms.ValidationError("please minute should be 00 .")                         
#         return datetime
          
    
#     def clean_user(self):
#         user = self.cleaned_data["user"]
#         if user == "":
#             raise forms.ValidationError("This field is required. ")
#         return user
    
   