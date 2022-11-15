
from email import message
import imp
from django.core.mail import send_mail
import random
from . models import *

from django.conf  import settings

import random
import string

import random
import string
import uuid


user_pass= ""
def passwordgen():
    global passw
    length = 7
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    all = lower + upper + num + symbols
    temp = random.sample(all,length)
    password = "".join(temp)
    return password
user_pass =passwordgen()




def send_login_email(email):
    subject = 'Your account login Password mail'
    message = f'Your password is  {user_pass}'  
    email_from = settings.EMAIL_HOST
    send_mail(subject, message, email_from, [email])




def send_forgetpassword_email(email,token):
    subject = "Your Reset Password Link "
    message = f'Hi Click on the link to reset your password   http://127.0.0.1:8000/resetpassword/{token}/'
    email_from = settings.EMAIL_HOST
    recipient_list = [email]
    send_mail(subject, message, email_from,recipient_list)
    print("send Successfully")
    return True


    