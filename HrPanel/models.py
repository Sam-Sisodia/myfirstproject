from django.db import models
from Admin.models  import *

status = (
    ("Hold", 'Hold'),
    ("Selected", 'Selected'),
    ("Rejected", 'Rejected'),)


# Create your models here.

class Office_meeting(models.Model):
    Meeting_Agenda=models.CharField( max_length=50)
    Description=models.TextField() 
    datetime= models.DateTimeField( auto_now=False, auto_now_add=False)
    user = models.ManyToManyField(User, related_name='user_office_meeting' )
    soft_delete=models.BooleanField(default=False)  #softdelete


    
class Interview_meeting(models.Model):
    first_name=models.CharField(max_length=120)
    last_name=models.CharField( max_length=50)
    soft_delete=models.BooleanField(default=False)                        #softdelete 
    user_cv=models.FileField( upload_to='cv', max_length=100,null=True,blank=True)
    email=models.EmailField( max_length=254)
    phone=models.IntegerField()
    datetime= models.DateTimeField(auto_now=False, auto_now_add=False)
    user = models.ManyToManyField(User, related_name='user_Interview_meeting')
    domain=models.ForeignKey(Domain_name, on_delete=models.CASCADE)
    position=models.CharField(max_length=10,choices=positon)
    status=models.CharField(max_length=10,choices=status,default="Hold",blank=True)
    attempt=models.CharField(max_length=50,null=True,blank=True)
    
  