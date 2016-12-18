# -*- coding:utf-8 -*-
from django import forms
from .models import User
from django.forms import ModelForm
from django.forms.utils import ErrorDict
from django.core.exceptions import ValidationError

class RegForm(forms.Form):
    # def validate_password(value):
    #     if value == "123456":
    #         raise ValidationError(u'%s is private,dont input' % value)

    username = forms.CharField(
        label = ("登录账号"),
        widget=forms.TextInput(
        attrs={"placeholder":"username","required":"required","class":"name","name":"name"}),
        max_length=15,min_length=6,
        error_messages={"required":"username不能为空","invalid":"用户名格式错误",
                        "min_length":"用户名最少6个字符",
                        "max_length":"用户名最多15个字符",},)
    #user_nickname = forms.CharField()

    password = forms.CharField(
        label=("密码"),
        widget=forms.PasswordInput(
        attrs={"placeholder":"password","required":"required","class":"password","name":"password"},),
        max_length=40,min_length=6,
        error_messages={"required":"password不能为空",},)
        #validators=[validate_password])

    user_password_2 = forms.CharField(
        label=("确认密码"),
        widget=forms.PasswordInput(
        attrs={"placeholder": "password confirm", "required": "required", "class": "password", "name": "password"}),
        max_length=40, min_length=6,
        error_messages={"required": "password不能为空"})

    email = forms.EmailField(
        label=("email"),
        widget=forms.TextInput(
            attrs={"placeholder": "email", "required": "required", "class": "name", "name": "email"}),
        error_messages={"required": "email不能为空", "invalid":"邮箱格式错误",},)

    def clean_user(self):
        user = self.cleaned_data.get('username')
        if user == 'cccccc':
            raise forms.ValidationError('用户名是我的')
        return user

    def clean(self):
        userall = User.objects.all()
        if not self.is_valid():
            print("")
            raise forms.ValidationError(u"所有项都为必填项")
        elif self.cleaned_data['username'] in User.objects.all().values('username'):
            print("wrong message1")
            raise forms.ValidationError(u"form表单用户已存在")
        elif self.cleaned_data['password'] != self.cleaned_data['user_password_2']:
            print("wrong message2")
            self._errors['password'] = self.error_class([u"两次输入的新密码不一样!"])
            raise forms.ValidationError(u"两次输入的新密码不一样")
        # elif self.cleaned_data['email'] :
        #     print("wrong message3")
        #     self._errors['email'] = self.error_class([u"邮箱格式不正确"])
        #     raise forms.ValidationError(u"邮箱格式不正确")
        else:
            print("wrong message4")
            cleaned_data = super(RegForm, self).clean()
        return cleaned_data

    # def clean(self):
    #     clean_data = self.cleaned_data
    #     pwd1 = self.clean_data['password']
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