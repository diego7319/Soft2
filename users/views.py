from django.contrib.auth import login, authenticate
from django.shortcuts import render,  redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from users.forms import Login, Signup
from django.contrib.auth.models import User


def index(request):
    formaLogin = Login()
    formaRegistro = Signup()
    if request.method == 'POST':
        if request.POST.get('submit') == 'login':
            print ('LOGINN')
            formaLogin = Login(request.POST)
            if formaLogin.is_valid():
                datos = formaLogin.cleaned_data
                username = datos.get('user')
                password = datos.get('password')
                print(username)
                print(password)
                user = authenticate(request,username=username,password=password)
                print (user)
                if user is not None:
                    login(request, user)
                    request.session.set_expiry(30)
                    return HttpResponse('login')
                else:
                    return HttpResponse('usuario no existe')
            else:
                return HttpResponse('error al loguear')
        elif request.POST.get('submit') == 'signup':
            formaRegistro = Signup(request.POST)
            if formaRegistro.is_valid():
                datos = formaRegistro.cleaned_data
                raw_username = datos.get('user')
                raw_password= datos.get('password');
                try:
                    user = User.objects.create_user(username=raw_username,password=raw_password)
                    user.save();
                    return HttpResponse('registrado')

                except:
                    return HttpResponse('username duplicado')

                return HttpResponse('error al registrar' )


    else:

        context = {
        'formaL': formaLogin,
        'formaS': formaRegistro
        }
        return render(request, 'index.html', context)
