
from django import forms
from . models import *
from . email import *
from HrPanel .models import *

class UserRegistarionForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','Employee_code','soft_delete','address','phone',
                  'usertype','position','domain',]


        def clean_username(self):
            username = self.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError("Username Already exits ")
            return username


class Desiganationform(forms.ModelForm):
    class Meta:
        model = Domain_name
        fields =   ['domain_name']
    
    def clean_domain_name(self):
        domain_name= self.cleaned_data['domain_name']
        obj = Domain_name.objects.filter(domain_name=domain_name,soft_delete=True).exists()
        if obj:
            Domain_name.objects.filter(domain_name=domain_name).update(soft_delete = False )
            
        else:
            pass

            
        return domain_name
     


class interviewform(forms.ModelForm):
    class Meta:
        model =   Interview_meeting
        fields = ['first_name','last_name','user_cv','email','phone','datetime','user','position',
                      'domain','status','attempt']
     

        
           




        
        
   

       


    # def clean_username(self):
    #     valfirstname = self.cleaned_data['username'] 
    #     print(valfirstname)
    
    #     # if len(valfirstname)<4  or valfirstname=="":
    #     #     raise forms.ValidationError("Eneter more then or equal to 4 charecter")

    #     return valfirstname

    # def clean_email(self):    
    #     validateemail = self.cleaned_data['email']
    #     if User.objects.filter(email=validateemail).exists():
    #            raise forms.ValidationError("Email already exist")
    #     return validateemail 

    # def clean_email(self):    
    #     validateemail = self.cleaned_data['email']
    #     if User.objects.filter(email=validateemail).exists():
    #            raise forms.ValidationError("Email already exist")
    #     return validateemail 
