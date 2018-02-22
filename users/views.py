from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render,  redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from users.forms import Login, Signup
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from grupos import views
from django.http import JsonResponse
from users.models import usuariocuenta
from analitica.models import CrearGrupoAccion
from analitica.acciones import log_accion_ver, log_accion_registro, log_accion_login, log_accion_logout
from analitica.acciones import get_accion_ver, get_accion_registro, get_accion_login, get_accion_logout,get_accion_invitar, get_accion_crear_grupo, get_accion_rpta_invitacion


def games(request):
    personas = [
        { 'nombre' : 'Juanita', 'edad' : 20 },
    ]
    variables = {
        'lista_personas' : personas
    }
    log_accion_ver(request.mongo_db, None, 'games')
    return render(request, 'games.html', variables)

def index(request):
    formaLogin = Login()
    formaRegistro = Signup()
    if request.method == 'POST':
        return (pLogin(request))
    else:
        if request.user.is_authenticated:
            return redirect('perfil')
        else:
            context = {
            'formaL': formaLogin,
            'formaS': formaRegistro
            }
            log_accion_ver(request.mongo_db, None, 'index')
            return render(request,'index.html', context)

def perfil(request):
    usern=request.user.username
    if not request.user.is_authenticated:
        return redirect('index')
    else:
        saldo= usuariocuenta.objects.get(usuario=request.user.username)
        if request.method=='POST':
            print (request)
            context = {'Invitaciones': views.invitaciones(usern),
            'grupos': views.useradmingroup(request.user.username),
            'misgrupos':views.misgrupos(request.user.username),
            'listausuarios':views.usuariosgrupo(request.POST.get('sometext')),
            'saldo':saldo.dinerocuenta
            }
            log_accion_ver(request.mongo_db, request.user.username, 'perfil')
            return render(request,'hom.html',context)
        else:

            context = {'Invitaciones': views.invitaciones(request.user.username),
            'grupos': views.useradmingroup(request.user.username),
            'misgrupos':views.misgrupos(request.user.username),
            'saldo':saldo.dinerocuenta

            }
            log_accion_ver(request.mongo_db, request.user.username, 'perfil')
            return render(request,'hom.html',context)

def log_out(request):
    log_accion_logout(request.mongo_db, request.user.username)
    logout(request)
    return redirect('index')

#recargarcuenta
def recargarcuenta(request):
    user= usuariocuenta.objects.get(usuario=request.user.username)
    saldoactual=user.dinerocuenta
    cantidadrecarga=float(request.POST.get('cantidadarecargar'))
    print (cantidadrecarga)
    user.dinerocuenta=(saldoactual+cantidadrecarga)
    user.save()
    return redirect('perfil')

def recargarcuentaCustom(ruser,cantidad):
    user= usuariocuenta.objects.get(usuario=ruser)
    saldoactual=user.dinerocuenta
    cantidadrecarga=cantidad
    user.dinerocuenta=(saldoactual+cantidadrecarga)
    try:
        user.save()
    except Exception as e:
        print ("Error en recargar cuenta : Usuario --> %s cantidad--> %s" % (ruser,cantidad))



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
                #request.session.set_expiry(3600)
                log_accion_login(request.mongo_db, user.username)
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
                cuenta=usuariocuenta(usuario=raw_username,dinerocuenta=10)
                cuenta.save();
                log_accion_registro(request.mongo_db, user.username)
                context['estadoregistro']='Registrado correctamente'
                print('dd')
                return render(request,'index.html',context)
            except:
                context['estadoregistro']='Usuario ya existe'
                return render(request,'index.html',context)
        else:
            context['estado']='Error de servidor.'
            return render(request,'index.html',context)
    else:
        return HttpResponse('no es un post aceptado')

def templateAnalitica(request):
    return render(request,'analitica.html')

def getAnalitica(request):
    ver = get_accion_ver(request.mongo_db)
    registro = get_accion_registro(request.mongo_db)
    login = get_accion_login(request.mongo_db)
    logout = get_accion_logout(request.mongo_db)
    invitar = get_accion_invitar(request.mongo_db)
    crear_grupo = get_accion_crear_grupo(request.mongo_db)
    rpta_invitacion = get_accion_rpta_invitacion(request.mongo_db)
    #for doc in res:
    #    print(doc)
    jsonrespuesta={'ver': ver , 'registro' : registro, 'login' : login, 'logout':logout, 'invitar':invitar, 'crear_grupo': crear_grupo, 'rpta_invitacion':rpta_invitacion }
    return JsonResponse(jsonrespuesta)
