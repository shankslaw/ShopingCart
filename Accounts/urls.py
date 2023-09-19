from django.urls import path,include
from . import views

app_name = 'Accounts'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('ForgotPassword/',views.forgot,name='forgot'),
    path('logout/',views.logoutt,name='logout')
]