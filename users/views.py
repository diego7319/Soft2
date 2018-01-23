from django.shortcuts import render,  redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from users.forms import Login, Signup
from users.models import Usuario


def index(request):
    lista = Usuario.objects.all()
    print ("");print ("");print ("");print ("");print("");print ("");print ("")

    for i in lista:
        print (i.user)

    formaLogin = Login()
    formaRegistro = Signup()
    if request.method == 'POST':
        if request.POST.get('submit') == 'login':
            print ('LOGINN')
            formaLogin = Login(request.POST)
            if formaLogin.is_valid():
                datos = formaLogin.cleaned_data
                rusername=datos.get('user')
                rpassword= datos.get('password')

                user = authenticate(username=rusername, password=rpassword)
                login(request, user)
                return redirect('home')

        elif request.POST.get('submit') == 'signup':
            formaRegistro = Signup(request.POST)
            print ('REGISTRO')
            #datos = formaLogin.cleaned_data
            print (formaRegistro)
            if formaRegistro.is_valid():
                datos = formaRegistro.cleaned_data
                formaRegistro.save()
                rusername=datos.get('user')
                rpassword= datos.get('password')

                print (rusername+"  "+rpassword)
                user = authenticate(request, username=rusername, password=rpassword)


                if user is not None:
                    #login(request, user)
                    return render(request, 'guard')

    else:

        context = {
        'formaL': formaLogin,
        'formaS': formaRegistro
        }
        return render(request, 'index.html', context)

"""
def login(request):
    formaLogin = Login(request.POST or None)
    if formaLogin.is_valid():

        datos = formaLogin.cleaned_data
        rusername=datos.get('user')
        rpassword= datos.get('password')
        user = authenticate(username=rusername, password=rpassword)
        login(request, user)
        return redirect('home')
    else:
        return redirect('/index')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
"""
