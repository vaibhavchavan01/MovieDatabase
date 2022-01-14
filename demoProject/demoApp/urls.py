from django.contrib.auth import login, views as auth_views
from django.urls import path
from . import views

# from django.views.generic import TemplateView
app_name = 'demoApp'

urlpatterns = [
    path('',views.HomepageView.as_view(),name='home'),
    path('signup1/',views.SignUpView.getUser,name='signup1'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('login1/',views.LoginCheckView.check_login,name= 'login1'),
    path('index/',views.AfterLoginView.as_view(), name='index'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('forget_password/',views.ForgetPasswordView.as_view(), name = 'forget_password'),
    path('getlink/',views.ForgetPasswordView.get_link,name='getlink'),
]
