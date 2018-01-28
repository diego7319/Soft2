from django.shortcuts import render
from django.contrib.auth.models import User #, Group
from grupos.models import grupo,Invitacion
from django.shortcuts import redirect
from django.contrib import messages
from users import views



# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
#document.location.href="/";
def invitarusuario(request):
    info = request.POST

    invi=info.get('invitado','')
    grp=info.get('grupo','')
    username = request.user.username
    invitadoexiste= User.objects.filter(username=invi).count()
    obj = Invitacion.objects.get(grupo=grp,invitado=invi).count()
    if admingrupos(username,grp)==True and invitadoexiste==1:
        invit=Invitacion(invitado=invi,grupo=grp)
        invit.save()
        return HttpResponse("<script>alert('Se envio invitacion');document.location.href='/perfil';</script>")
    elif obj>=1:
        return HttpResponse("<script>alert('invitacion ya existe');document.location.href='/perfil';</script>")
    else:
        return HttpResponse("<script>alert('Usuario o grupo no existe');document.location.href='/perfil';</script>")

def agregargrupo(request):
    username = request.user.username
    info = request.POST
    gr=info.get('nombregrupo','')
    lista = grupo.objects.filter(nombre=gr).count()
    if lista ==1:
        #messages.info(request, 'Grupo ya existe')
        #return views.perfil(request)
        return HttpResponse("<script>alert('Grupo ya existe');document.location.href='/perfil';</script>")

    else:
        db_registro = grupo(nombre=gr,owner=username);
        db_registro.savee()
        messages.info(request, 'Grupo creado')
        #return views.perfil(request)
        return HttpResponse("<script>alert('Grupo creado');document.location.href='/perfil';</script>")












""" Funcionaes de apoyo"""
#Crea un grupo


#lista de usuarios de un grupo
def listausuarios(rgrupo):
    lista = Invitacion.objects.filter(invitado=nombre)
    gp = grupo.objects.filter(nombre=rgrup).count()
    invitaciones=[]
    grupos=[]
    for i in lista:
        if i.estado=='aceptado':
            print (0)
    pass
    #return HttpResponse()

#si el nombre es administrador de grupo retorna true
def admingrupos(nombre,rgrupo):
    lista= grupo.objects.filter(owner=nombre,nombre=rgrupo).count()
    if lista==1:
        return (True)
    else:
        return False

#se envia el pedido de
def invitaciones(ruser):
    p=Invitacion.objects.filter(invitado=ruser,estado='pendiente')
    datos=[]
    for i in p:
        datos.append(i.grupo)
    return datos

def responderinvitacion(request):
    info = request.POST
    rgrupo=info.get('grupo')
    ruser=request.user.username
    rpta=info.get('rpta')
    obj = Invitacion.objects.get(grupo=rgrupo,invitado=ruser,)
    print (obj.estado)
    obj.estado=rpta
    obj.save()
    print (obj.estado)
    if rpta=='aceptado':
        return HttpResponse("<script>alert('Grupo aceptado');document.location.href='/perfil';</script>")
    else:
        return HttpResponse("<script>alert('Grupo rechazado');document.location.href='/perfil';</script>")
