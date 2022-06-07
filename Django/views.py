from email import message
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from users.models import NewUser
from django.core.mail import send_mail



def home(request):
    return render(request, 'Jango.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(email=email,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('main-page')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')

def reg(request):

    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if NewUser.objects.filter(email=email).exists():
                return redirect('reg')
            else:
                password = password1
                user = NewUser.objects.create_user(email=email,password=password)
                user.save()
        else:
            return redirect('login')
        return redirect('main-page')
    else:
        return render(request, 'reg.html')


def Logout(request):
    auth.logout(request)
    return render(request, 'login.html')


def mainpage(request):
    return render(request, 'mainpage.html')

def userpage(request):
    return render(request, 'userpage.html')

def settings(request):
    return render(request, 'settings.html')

def analitics(request):
    return render(request, 'analitics.html')

def result(request):
    return render(request, 'result.html')



def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message = request.POST['message']
        message_to_email = request.POST['message-to-email']
        
        send_mail(
            message_name,
            message,
            [message_to_email]
        )
        
        
        return render(request, 'contact.html', {'message_n'})
        
    else:
        return render(request, 'contact.html', {})
