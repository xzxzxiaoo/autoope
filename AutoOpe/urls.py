"""AutoOpe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from autoo.upload import upload_image
from autoo import views
from django.conf import settings
#from django.contrib.auth.views import logout


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #设置头像
    url(r'^admin/upload/(?P<dir_name>[^/]+)/',upload_image,name='upload_image'),
    #头像
    url(r"uploads/(?P<path>.*)$", \
        "django.views.static.serve", \
        {"document_root": settings.MEDIA_ROOT,}),
    #url(r'^user_head_pic/(?P<dir_name>[^/]+)/', upload_image, name='user_image'),
    #引入autoo模块中的urls
    #url(r'^$', include('autoo.urls')),

    url(r'^$', views.userlogin, name='userlogin'),


    #登录界面,
    #url(r"login/", views.userlogin, name='userlogin'),
    url(r'^manager/(?P<user_name>[^/]+)/$', views.manager, name='manager'),
    #登录注册界面
    url(r'register/', views.register, name='register'),
    # 登录注册界面
    url(r'logoutUser/', views.logoutUser, name='logoutUser'),
    #领导查看用户界面
    url(r'usermsg/', views.usermsg, name='usermsg'),

    #进入用户设置界面
    url(r'userinfo/', views.userinfo, name='userinfo'),
    #进入用户设置界面
    url(r'usersetting/', views.usersetting, name='usersetting'),
]
