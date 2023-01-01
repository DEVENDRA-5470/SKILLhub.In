from django.urls import path
from blog import views 
from blog.forms import Login_form, Set_password
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.Home.as_view(),name="home"),
    path('signup/',views.signup,name="signup"),
    path('logout/',views.Mylogout.as_view(),name='logout'),
    path('login/',views.Mylogin.as_view(),name='login'),
    path('update/<int:id>',views.detail,name='detail'),
    path('enroll_now/',views.enroll_now,name='enroll_now'), 
]
