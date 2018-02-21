from django.shortcuts import render
from django.contrib.auth.models import User #, Group
from grupos.models import grupo,Invitacion
from django.shortcuts import redirect
from users import views
from analitica.acciones import log_accion_invitar, log_accion_crear_grupo, log_accion_rpta_invitacion



# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
#document.location.href="/";
def invitarusuario(request):
    if not request.user.is_authenticated:
        return redirect('index')
    info = request.POST
    invi=info.get('invitado','')
    grp=info.get('grupo','')
    username = request.user.username
    invitadoexiste= User.objects.filter(username=invi).count()
    obj= 0
    obj = Invitacion.objects.filter(grupo=grp,invitado=invi).count()

    if obj>=1:
        return HttpResponse("<script>alert('invitacion ya existe');document.location.href='/perfil';</script>")
    elif admingrupos(username,grp)==True and invitadoexiste==1:
        invit=Invitacion(invitado=invi,grupo=grp)
        invit.save()
        log_accion_invitar(request.mongo_db, username, invi, grupo)
        return HttpResponse("<script>alert('Se envio invitacion');document.location.href='/perfil';</script>")
    else:
        return HttpResponse("<script>alert('Usuario o grupo no existe');document.location.href='/perfil';</script>")

def agregargrupo(request):
    if not request.user.is_authenticated:
        return redirect('index')
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
        db_registro.save()
        inv= Invitacion(invitado=username,owner=username,estado='aceptado',grupo=gr)
        inv.save()
        log_accion_crear_grupo(request.mongo_db, username, gr)
        #return views.perfil(request)
        return HttpResponse("<script>alert('Grupo creado');document.location.href='/perfil';</script>")

#aceptar o rechazar invitacion
def responderinvitacion(request):
    if not request.user.is_authenticated:
        return redirect('index')
    info = request.POST
    rgrupo=info.get('grupo')
    ruser=request.user.username
    rpta=info.get('rpta')
    obj = Invitacion.objects.get(grupo=rgrupo,invitado=ruser)
    obj.estado=rpta
    obj.save()
    if rpta=='aceptado':
        log_accion_rpta_invitacion(request.mongo_db, ruser, rgrupo, True)
        return HttpResponse("<script>alert('Grupo aceptado');document.location.href='/perfil';</script>")
    else:
        log_accion_rpta_invitacion(request.mongo_db, ruser, rgrupo, False)
        return HttpResponse("<script>alert('Grupo rechazado');document.location.href='/perfil';</script>")


""" Funcionaes de apoyo"""

#lista de usuarios de un grupo
def listausuarios(rgrupo):
    nombre='aceptado'
    lista = Invitacion.objects.filter(group=rgrupo,invitado=nombre)
    #gp = grupo.objects.filter(nombre=rgrup).count()
    usuarios=[]
    pass
    #return HttpResponse()

#si el nombre es administrador de grupo retorna true
def admingrupos(nombre,rgrupo):
    lista= grupo.objects.filter(owner=nombre,nombre=rgrupo).count()
    if lista==1:
        return (True)
    else:
        return False

#retorna invitaciones pendientes
def invitaciones(ruser):
    p=Invitacion.objects.filter(invitado=ruser,estado='pendiente')
    datos=[]
    for i in p:
        datos.append(i.grupo)
    return datos

#retorna los grupos donde el usaurio es admin
def useradmingroup(ruser):
    rpta=[]
    lista= grupo.objects.filter(owner=ruser)
    for i in lista:
        rpta.append(i.nombre)
    return rpta

#retorna una lista de los grupos a los que pertenece un usuario
def misgrupos(ruser):
    rpta=[]
    lista= Invitacion.objects.filter(invitado=ruser,estado='aceptado')
    for i in lista:
        if i.estado=='aceptado':

            rpta.append(i.grupo)
    return rpta
#retorna usuarios de un grupo
def usuariosgrupo(rgrupo):
    rpta=[]
    lista = Invitacion.objects.filter(grupo=rgrupo)
    for i in lista:
        if i.estado=='aceptado':
            rpta.append(i.invitado)
    return rpta
