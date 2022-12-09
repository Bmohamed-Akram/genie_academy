from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect, render

from Home.views import test


# Create your views here.
def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This username is already taken try another one')
                return redirect('Register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'This email is already taken try another one')
                return redirect('Register')

            else:
                user = User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                messages.info(request,'account created successfully')
                return redirect('Login')

        else:
            messages.info(request,'Passwords are not same try again')
            return redirect('Register')

    else:
        return render(request,'Login/register.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('test')

        else:
            messages.info(request,'No user found')
            return redirect('Login')

    else:
        return render(request,'Login/index.html')

def Logout(request):
    auth.logout(request)
    return redirect('test') 
