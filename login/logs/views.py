from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
# Create your views here.
def hello(request):
    return HttpResponse ('hello World !')



def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        passw = request.POST.get('password')
        # re_pass= request.POST.get('repassword')
        user = User.objects.create_user(username,email,passw)
        user.first_name= username
        user.save()
        messages.success(request, "Signup Successfull !")
        return redirect ('userlogin')
    return render(request, 'reg.html')

        



def userlogin(request):
    if request.method == "POST":
        your_name = request.POST.get('your_name')
        your_pass = request.POST.get('your_pass')
        user = authenticate(username=your_name, password=your_pass)

        if user is not None:
            auth_login(request, user)
            #username = user.first_name
            return redirect ('portfolio')
        else:
            messages.error(request, "Wrong Credentials !" )
            return redirect('logout')
        
    return render(request, 'log.html')
def logout(request):
    auth_logout(request)
    return render(request, 'log.html')
def portfolio(request):
    return render(request, 'portfolio.html')

    