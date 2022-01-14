from django.contrib.auth.forms import UsernameField
# from . import forms
import uuid
from django.db import models
from django.views.generic import TemplateView
from django.http import HttpResponse, request
from django.urls import reverse_lazy
from .models import User
from django.contrib.auth import login, logout
from django.shortcuts import render
from .forms import UserCreateForm, UserForm
from .emailSetup import forget_password_mail

class SignUpView(TemplateView): 
      
    form_class = UserCreateForm
    # success_url = reverse_lazy("login")
    # success_url1 = "hello1122"
    template_name = "signup.html"
    # def get(self, request, **kwargs):     
    #     print(request)
    #     return render(request, 'signup.html')
    
    def getUser(request):
        if request.method=='POST':
            userData = User(
                firstname = request.POST.get('fname'),
                lastname = request.POST.get('lname'),       
                email = request.POST.get('email'),
                mobile = request.POST.get('mobile'),
                password = request.POST.get('psw'),
                confirm_password = request.POST.get('psw-repeat')
            )
            userData.save()
        # print(firstname)
        return render(request, 'login.html')
        # user=User.objects.get(email=email)
class LoginCheckView(TemplateView):
    form_class = UserForm
    # template_name = 'login.html'
    
       
    def check_login(request):
        user = ''
        if request.method == 'POST':
            login_user = request.POST.get('uname')
            login_password = request.POST.get('psw')
            # user = self.get_user(login_user)
            if login_user.isdigit():
                user = User.objects.get(mobile=login_user)
            else:
                user = User.objects.get(email=login_user)    
            # print(user.mobile, user.email, user.confirm_password)
            if login_password  == user.password:
                return render(request, 'index.html')
            else:
                return render(request, 'login.html')
class ForgetPasswordView(TemplateView):
    template_name = 'forget_password.html'
    def get_link(request):
        token = str(uuid.uuid4())
        if request.method == 'POST':
            email = request.POST.get('uname')
            user = User.objects.get(email=email)    
            if email == user.email:
                forget_password_mail(email, token)
            else:
                messages.success(request, 'User not found with this username')
                # pass

class HomepageView(TemplateView):
    template_name = "homepage.html"
    # pass
class AfterLoginView(TemplateView):
    # Template_name = "forget_password.html"
    pass
class GetResetLink(TemplateView):
    pass