# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Power(models.Model):
    power_name = models.CharField(max_length=10, null=False, unique=True,verbose_name = '权限名称')

    class Meta:
        verbose_name = '权限'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.power_name

class Role(models.Model):
    role_name = models.CharField(max_length=30, null=False, unique=True, verbose_name='角色名称')
    role_power = models.ForeignKey(Power, verbose_name='角色权限')

    class Meta:
        verbose_name = '角色'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.role_name


class User(AbstractUser):
    #user_userloginname = models.CharField(max_length=15,null=False,unique=True,verbose_name='用户名称')
    #user_nickname = models.CharField(max_length=10,null=True,unique=False,verbose_name='昵称')
    #user_password = models.CharField(max_length=15,null=False,unique=False,verbose_name='密码')
    user_phone = models.IntegerField(null=True,unique=True,verbose_name='用户电话')
    user_role_name = models.ForeignKey(Role,null=True, on_delete=models.CASCADE, verbose_name='角色名称')
    user_describe = models.TextField(max_length=150,blank=True,null=True,verbose_name='用户描述')
    user_avatar = models.ImageField(upload_to='avatar/%Y/%m',default='avatar/default.png',max_length=200,blank=True,null=True,verbose_name='用户头像')
    user_register_time = models.DateField(null=True,verbose_name='用户注册时间')


    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class GroupManager(models.Model):
    group_name = models.CharField(max_length=30,null=False,unique=True,verbose_name='群名称')
    group_power = models.ForeignKey(Power, verbose_name='群权限')

    class Meta:
        verbose_name = '群'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.group_name


class UserGroup(models.Model):
    groupname = models.ManyToManyField(GroupManager,verbose_name='群名称')
    manageruser = models.ManyToManyField(User,verbose_name='用户')


    class Meta:
        verbose_name = '用户群管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.groupname

class Message(models.Model):
    message_content = models.TextField(max_length=500,verbose_name='信息')
    class Meta:
        verbose_name = '相关信息'
        verbose_name_plural = verbose_name

    def __str__(self):
         return self.message_content

#
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='被通知用户')
    Message = models.ForeignKey(Message,  on_delete=models.CASCADE, verbose_name='发送的信息')
    Notification_sendtime = models.DateField(null=False, verbose_name='通知发送时间')

    class Meta:
        verbose_name = '通知'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class UserSendMessage(models.Model):
    send_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='信息')
    message_sendtime = models.DateField(null=False, verbose_name='通知发送时间')
    class Meta:
        verbose_name = '发送信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class LocationServer(models.Model):
    location_name = models.CharField(max_length=30,null=True,unique=False,verbose_name='地址名称')

    class Meta:
        verbose_name = '服务器地址'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Project(models.Model):
    project_name = models.CharField(max_length=30,null=True,unique=False,verbose_name='项目名称')
    project_power = models.ForeignKey(Power,on_delete=models.CASCADE,verbose_name='项目权限')
    project_create_time = models.DateField(null=False, verbose_name='项目创建时间')

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.power_name

class ProjectforUser(models.Model):
    user = models.ManyToManyField(User,verbose_name='用户')
    project = models.ManyToManyField(Project,verbose_name='项目')

    class Meta:
        verbose_name = '项目所属管理人员'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Server(models.Model):
    server_name = models.CharField(max_length=30,null=True,unique=False,verbose_name='服务器名称')
    server_ip = models.GenericIPAddressField(null=False,unique=True,verbose_name='服务器IP地址')
    server_port = models.IntegerField(null=False,unique=False,verbose_name='服务器端口')
    server_login_username = models.CharField(max_length=30,null=True,unique=False,verbose_name='服务器登录名')
    server_login_password = models.CharField(max_length=30, null=True, unique=False, verbose_name='服务器密码')
    server_location = models.ForeignKey(LocationServer,null=True, on_delete=models.CASCADE,verbose_name='项目位置')
    server_project= models.ForeignKey(Project,null=True, on_delete=models.CASCADE,verbose_name='项目')

    class Meta:
        verbose_name = '服务器'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class ServerforUser(models.Model):
    user = models.ManyToManyField(User,verbose_name='用户')
    server = models.ManyToManyField(Server,verbose_name='服务器')

    class Meta:
        verbose_name = '用户所管理的服务器'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name