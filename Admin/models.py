
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
import time
# Create your models here.
from datetime import datetime    


class Domain_name(models.Model):
    domain_name = models.CharField(max_length=25,unique=True)
    created_at =  models.DateTimeField(auto_now_add= True)
    soft_delete = models.BooleanField(default=False)


    def __str__(self):
        return self.domain_name


user_role  = (
        ("Admin", "Admin"),
        ("HR", 'HR'),
        ("MD", 'MD'),
        ("TL","TL"),
        ("Intern",'Intern'),
        ("Employee", "Employee") )


positon = (
    ("Sr", "Sr"),
    ("Jr", 'Jr'),
    ("Intern", 'Intern'),
    )


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Employee_code = models.IntegerField(unique=True,null=True,blank=True)
    soft_delete = models.BooleanField(default=False)
    address=models.CharField( max_length=520)
    phone = models.CharField(max_length=100, null=True, blank=True)
    usertype = models.CharField(max_length=10 , choices= user_role)
    position = models.CharField(max_length=10 , choices= positon)
    domain=models.ForeignKey(Domain_name, on_delete=models.CASCADE,null=True, blank=True)
    def __str__(self):
         return self.username
     
     

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    forget_password_token = models.CharField( max_length=520)
    created_at =  models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.user.username