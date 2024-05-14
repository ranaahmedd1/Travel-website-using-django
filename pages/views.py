from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Traveller
from tours.models import Cities

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def login(request):
    if request.method =='POST':
        userLogin = request.POST.get('user')
        passwrdLogin = request.POST.get('passwrd')
        all_users = Traveller.objects.all().filter(username=userLogin,password=passwrdLogin)
        if all_users : 
            request.session["user"] = userLogin 
            request.session.set_expiry(9000) 
            return redirect('tours')#,{'data':enumerate(Cities.objects.all()) })
        else:
            return render(request, 'pages/login.html',{'resultMSG':'Invalid username or password'})
    else:
        if "user" in request.session:
            return redirect('tours')#,{'data':enumerate(Cities.objects.all()) })
        return render(request, 'pages/login.html')

def signup(request):
    if request.method == 'POST':
        username= request.POST.get('Username')
        email=request.POST.get('email')
        paswrd= request.POST.get('passwrdinput')
        Confpaswrd= request.POST.get('ConfirmPasswrd')
        newSignup=Traveller(username=username,email=email,password=paswrd,Confpassword=Confpaswrd)  
        newSignup.save()
        return render(request, 'pages/login.html')

    return render(request, 'pages/signup.html')



def logout(request):
        del request.session["user"]
        return redirect ('login')




