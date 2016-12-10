# -*- coding:utf-8 -*-
from django import forms
from .models import User
from django.forms import ModelForm
from django.forms.utils import ErrorDict
from django.core.exceptions import ValidationError

class RegForm(forms.Form):
    username = forms.CharField(
        label = ("登录账号"),
        widget=forms.TextInput(
        attrs={"placeholder":"username","required":"required","class":"name","name":"name"}),
        max_length=15,min_length=6,
        error_messages={"required":"username不能为空","invalid":"用户名格式错误",
                        "min_length":"用户名最少6个字符",
                        "max_length":"用户名最多15个字符",},)
    #user_nickname = forms.CharField()

    user_password_1 = forms.CharField(
        label=("密码"),
        widget=forms.PasswordInput(
        attrs={"placeholder":"password","required":"required","class":"password","name":"password"}),
        max_length=40,min_length=6,
        error_messages={"required":"password不能为空"})

    user_password_2 = forms.CharField(
        label=("确认密码"),
        widget=forms.PasswordInput(
        attrs={"placeholder": "password confirm", "required": "required", "class": "password", "name": "password"}),
        max_length=40, min_length=6,
        error_messages={"required": "password不能为空"})

    def clean_user(self):
        user = self.cleaned_data.get('user_userloginname')
        if user == 'cccccc':
            raise forms.ValidationError('用户名是我的')
        return user

    # def clean(self):
    #     clean_data = self.cleaned_data
    #     pwd1 = self.clean_data['user_password_1']
    #     pwd2 = self.clean_data['user_password_2']
    #     print(pwd1,pwd2)
    #     if  pwd1 != pwd2:
    #         print('两次不一样')
    #         raise forms.ValidationError('password confirm failed')
    #     return clean_data

    #user_phone = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder":"phone","required":"required","class":"password","name":"email"}),error_messages={"required":"email不能为空"})
    #user_email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder":"email","required":"required","class":"name","name":"email"}),error_messages={"required":"email不能为空"})
    #user_role_name = forms.
    #user_describe = forms.Textarea()
    #user_avatar = forms.ImageField()
    #user_login_time = forms.DateField()
    #user_register_time = forms.DateField()



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"username","required":"required","class":"name","name":"name"}),max_length=40,error_messages={"required":"username不能为空"})
    user_password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"password","required":"required","class":"password","name":"password"}),max_length=40,error_messages={"required":"password不能为空"})