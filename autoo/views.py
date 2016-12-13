import logging
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.conf import settings
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from .models import *
from autoo.util.userlogin import *
from autoo.forms import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required



logger=logging.getLogger('autoo.views')
# Create your views here.
def global_setting(request):
    return {'SITE_NAME':settings.SITE_NAME,
            'SITE_DESC':settings.SITE_DESC,
            'PRO_EMAIL': settings.PRO_EMAIL,
            'INEDX_PAGE':settings.INEDX_PAGE,
            'MANAGER_DIR': settings.MANAGER_DIR,}


def userlogin(request):
    try:
        print("login1")
        if request.method=='POST':
            print("login1.1")
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                print("login1.2")
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['user_password']
                print(username,password)
                user = authenticate(username=username, password=password)
                request.session['username'] = username
                print("login1.2.1")
                print(request.session['username'])

                print("login1.2.2")
                print(user)

                if user is not None:
                    print("login1.3")
                    user.backend = 'django.contrib.auth.backends.ModelBackend'
                    login(request, user)
                else:
                    print("login1.4")
                    return render(request, 'major/failure.html', locals())
                print("login1.5")
                #req= HttpResponseRedirect('major/failure.html')
                #req = render(request, 'major/index.html', locals())
                req = HttpResponseRedirect('manager/%s' %(request.user.username))


                req.set_cookie('username',username,max_age=11)
                return req


            else:
                print("login2")
                return render(request, 'major/failure.html', locals())
        else:
            login_form = LoginForm()
    except Exception as e:
        print("login3")
        logger.error(e)
    print("login4")
    return render(request, 'major/signin.html', locals())

def loginSuccess(request,user_name):
     try:
         print("success1")
         islogin = request.user.username
         print(request.session['username'])
         if request.user.username is not None:
            print("success2")
            return render(request, 'major/index.html',  locals())
         else:
             print("success3")
             return render(request, 'major/signin.html',  locals())
     except Exception as e:
         print("success4")
         logger.error(e)
     print("success5")
     return render(request, 'major/index.html',{'user_name':request.user.username}, locals())


def register(request):
    try:
        userall = User.objects.all().values('username')
        print(userall)

        if request.method=='POST':
            print("register1")

            reg_from = RegForm(request.POST)

            print(reg_from.clean().values())
            if reg_from.is_valid():

                #b = UserAdd()
                #user = b.add(reg_from.cleaned_data['user_userloginname'], make_password(reg_from.cleaned_data['user_password']))

                user = User.objects.create(username=reg_from.cleaned_data['username'],
                                           password=make_password(reg_from.cleaned_data['password']),
                                           user_register_time=time.strftime('%Y-%m-%d', time.localtime(time.time())))



                print("register1.1")


                #print(registerForm.user_password_2)
                #print(registerForm.usename)
                print("register1.2")

                user.save()
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                print(user)

                login(request, user)
                print("register2")

                return render(request, 'major/index.html',locals())
                #username_web = request.session.get('username', request.user.username)
                #userRoleName_web = User.objects.get(username=username_web).user_role_name
            else:
                print("register3")
                print(reg_from.errors)
                print(reg_from.non_field_errors())
                return render(request, 'major/signup.html',locals())
        else:
            print("register4")

            reg_from = RegForm(request.POST)

    except Exception as e:
        print("register5")
        logger.error(e)
    print("register6")
    return render(request, 'major/signup.html', locals())



def logoutUser(request):
    try:

        logout(request)

    except Exception as e:
        print("logout2")
        logger.error(e)
    print("logout3")
    return render(request,'major/returnLogin.html',locals())


def manager(request,user_name):
    try:
        print("manager1")
        if request.user.is_authenticated():
            username_web = request.session.get('username', request.user.username)
            userRoleName_web = User.objects.get(username=username_web).user_role_name
            user_name = request.user.username


            #userrole = User.objects.get(user_role_name_id=1).username
            #role = Role.objects.get(role_name=1)
            print(userRoleName_web)
            #print(role)

            print("manager2")

            print(username_web)
            return render(request, 'major/index.html', locals())

    except Exception as e:
        logger.error(e)
    return render(request,'major/needlogin.html',locals())

def usermsg(request):
    try:
        username_web = request.session.get('username', request.user.username)
        userRoleName_web = User.objects.get(username=username_web).user_role_name
        user_list = User.objects.all()
        paginator = Paginator(user_list,5)
        try:
            page = int(request.GET.get('page',1))
            user_list = paginator.page(page)
        except(EmptyPage,InvalidPage,PageNotAnInteger) as e:
            user_list = paginator.page(1)
            logger.error(e)

        print("首页")
    except Exception as e:
        logger.error(e)
    return render(request,'major/usermsg.html',locals())

def userinfo(request):
    try:
        username_web = request.session.get('username', request.user.username)
        userRoleName_web = User.objects.get(username=username_web).user_role_name

        print("首页")
    except Exception as e:
        logger.error(e)
    return render(request,'major/userinfo.html',locals())

def usersetting(request):
    try:
        username_web = request.session.get('username', request.user.username)
        userRoleName_web = User.objects.get(username=username_web).user_role_name


        print("首页")
    except Exception as e:
        logger.error(e)
    return render(request, 'major/usersetting.html', locals())

