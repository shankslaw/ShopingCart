from collections import UserDict
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages


def user_login(request):
    print("hiiii")
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('password')
        print(request.POST.get('user'))
        print(request.POST.get('password')) 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("hiii")
            print(user)
            login(request, user)
            print('f')
            return redirect('/')  # Redirect to the home page after successful login
    
    return render(request, 'login.html')
# Create your views here.

def register(req):
    if req.method == 'POST' : 

        fname= req.POST.get('fname')
        lname= req.POST.get('lname')
        usrname = req.POST.get('user')
        password = req.POST.get('password1')
        re_password = req.POST.get('password2')
        email = req.POST.get('email')

        if password == re_password :
            reg = User.objects.create_user(last_name=lname, first_name=fname, username=usrname ,email=email ,password=password)
            reg.save()
            messages.success(req, f'Account created for {usrname}!')
            return redirect('/') 
    return render(req,'registeration.html')        

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('password')
        print(request.POST.get('user'))
        print(request.POST.get('password')) 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("hiii")
            print(user)
            login(request, user)
            print('f')
            return redirect('/')  # Redirect to the home page after successful login
    
    return render(request, 'login.html')

def forgot(req):
    if req.method == 'POST':
        entered_email = req.POST.get('en_mail')
        print(entered_email)
        new_password = req.POST.get('n_password1')
        
        try:
            print("try")
            user = User.objects.get(email=entered_email)
        except User.DoesNotExist:
            print("exce3pt")
            # Handle case when user does not exist
            return redirect('Accounts:forgot')

        if user.email == entered_email:
            # Change the user's password
            print("hiiiiiii")
            user.set_password(new_password)
            user.save()

            # Redirect or render a success message
            return redirect('/')
        else:
            # Handle case when entered email doesn't match user's email
            return redirect('/')
        
    return render(req,'forgotpassword.html')

def logoutt(req):
    logout(req)
    return redirect('Home:index')