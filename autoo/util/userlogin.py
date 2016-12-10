from autoo.models import User
from django.shortcuts import render
import xml.sax
import time

from autoo.forms import *

# class UserLogin:
#     def findByAll(self,*args,**kwargs):
#         t = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        # User.objects.create(user_userloginname=user_userloginname, user_password=user_password, user_register_time=t)
# class UserLogout:
#     def logout(self):
#         pass

class UserAdd:
    def add(self,*args,**kwargs):
        t = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        AUser.objects.create(user_userloginname=args[0],user_password=args[1], user_register_time=t)





