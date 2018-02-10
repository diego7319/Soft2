from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render,  redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from users.forms import Login, Signup
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from grupos import views
from users.models import usuariocuenta

def index(request):
    formaLogin = Login()
    formaRegistro = Signup()
    if request.method == 'POST':
        return (pLogin(request))
    else:
        context = {
            'formaL': formaLogin,
            'formaS': formaRegistro
            }
        return render(request,'index.html', context)

def perfil(request):
    usern=request.user.username
    if not request.user.is_authenticated:
        return redirect('index')

    else:
        if request.method=='POST':

            print (request)
            context = {'Invitaciones': views.invitaciones(usern),
            'grupos': views.useradmingroup(request.user.username),
            'misgrupos':views.misgrupos(request.user.username),
            'listausuarios':views.usuariosgrupo(request.POST.get('sometext'),)
            }
            return render(request,'hom.html',context)
        else:

            context = {'Invitaciones': views.invitaciones(request.user.username),
            'grupos': views.useradmingroup(request.user.username),
            'misgrupos':views.misgrupos(request.user.username)
            }
            return render(request,'hom.html',context)
def log_out(request):
    logout(request)
    return redirect('index')



""" Funciones de apoyo """
""" Funcion de login"""
def pLogin(request):
    formaLogin = Login()
    formaRegistro = Signup()
    if request.POST.get('submit') == 'login':
        formaLogin = Login(request.POST)

        if formaLogin.is_valid():
            datos = formaLogin.cleaned_data
            username = datos.get('user')
            password = datos.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                request.session.set_expiry(3600)
                return redirect('perfil/')
            else:
                context = {
                'formaL': formaLogin,
                'formaS': formaRegistro,
                'estadologin':'Usuario o contraseña incorrecto'
                }
                return render(request,'index.html',context)
    else:
        return pRegistro(request)


""" Funcion de Registro"""
def pRegistro(request):
    formaLogin = Login()
    formaRegistro = Signup()
    if request.POST.get('submit') == 'signup':
        formaRegistro = Signup(request.POST)
        if formaRegistro.is_valid():
            datos = formaRegistro.cleaned_data
            raw_username = datos.get('user')
            raw_password= datos.get('password');
            context = {
                'formaL': formaLogin,
                'formaS': formaRegistro
                }
            try:
                user = User.objects.create_user(username=raw_username,password=raw_password)
                user.save();
                cuenta=usuariocuenta.objects.create_user(username=raw_username,dinerocuenta=10)
                cuenta.save()
                context['estadoregistro']='Registrado correctamente'
                return render(request,'index.html',context)
            except:
                context['estadoregistro']='Usuario ya existe'
                return render(request,'index.html',context)
        else:
            context['estado']='Error de servidor.'
            return render(request,'index.html',context)
    else:
        return HttpResponse('no es un post aceptado')
