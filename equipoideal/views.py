from django.shortcuts import render
from .models import JugadorPais
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from django.http import JsonResponse
import json
from django.http import HttpResponse
from grupos.views import misgrupos,useradmingroup
from .models import salaequipoideal,PagoSalaEquipoIdeal
from grupos.models import Invitacion
# Create your views here.
#template de configuracion
def templateequipoideal(request):
    context={
    'misgrupos':useradmingroup(request.user.username),
    'usuario':request.user.username
    }
    return render(request,'configurarjuego.html',context)
#Juego
def JuegoEquipoIdeal(request):
    context={
    'usuario':request.user.username
    }
    return render(request,'jugar.html',context)
#Api de jugadores
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def retornarjugadores(request):
    datos={}
    if request.method == 'GET':
        return jugador_paisToJson()

#creacion de sala
def crearsalaEI(request):
    if not request.user.is_authenticated:
        return redirect('index')
    else:
        info=request.POST
        estado='activo'
        nombresala=info.get('nombresala')
        nombregrupo=info.get('grupo','')
        rpago=int(info.get('pago'))
        nombreusado={}
        if grupoexiste(nombresala)=='El nombre de la sala ya existe':
            nombreusado['existe']='El nombre de la sala ya existe,use otro nombre'
            nombreusado['misgrupos']=useradmingroup(request.user.username)
            nombreusado['usuario']=request.user.username
            return render(request,'configurarjuego.html',nombreusado)
        else:
            salaobj=salaequipoideal(nombreJuego=nombresala,grupo=nombregrupo,
            estado='activo',pago=rpago)
            salaobj.save()
            print (salaobj)
            GenerarPago(nombresala,rpago,nombregrupo)
            context={'misgrupos':useradmingroup(request.user.username),
            'existe':'Sala de juego creada',
            'usuario':request.user.username
            }
            return render(request,'configurarjuego.html',context)

def obtenerSalasEI(request):
    jsonrespuesta={}
    ruser=request.POST.get('usuario')
    listagrupos=misgrupos(ruser)
    salagrupo= getSalasdeGrupoEI(listagrupos)
    cont=0
    for i in salagrupo:
        jsonrespuesta[str(cont)]={'sala':i.split('-')[0],'grupo':i.split('-')[1],'estado':estadopago(i.split('-')[0],i.split('-')[1],ruser)}
        cont+=1
    return JsonResponse(jsonrespuesta)


def pagar_salaEI(request):
    info=request.POST
    rusuario=info['jugarusuario']
    rnombrejuego=info['jugarsala']
    rgrupo=info['jugargrupo']
    cantpagar=salatrivia.objects.get(nombreJuego=rnombrejuego,grupo=rgrupo).pago
    saldouser=usuariocuenta.objects.get(usuario=rusuario)
    if int(cantpagar) > int(saldouser.dinerocuenta):
        print (int(cantpagar) > int(saldouser.dinerocuenta))
        return JsonResponse({"rpta": "No hay saldo suficiente en tu cuenta"})
    else:
        nuevosaldouser=saldouser.dinerocuenta-cantpagar
        cambiarestado=PagoSala.objects.get(nombreJuego=rnombrejuego,grupo=rgrupo,user=rusuario)
        saldouser.dinerocuenta=nuevosaldouser
        saldouser.save()
        cambiarestado.estadopago='pagado'
        cambiarestado.save()
        return JsonResponse({"rpta": "Pago realizado"})

#metodos de apoyo
def jugador_paisToJson():
    cont=0;
    pais_jugadordict={}
    lista_paises=JugadorPais.objects.values('pais').distinct()
    for ipais in lista_paises:
        lista_jugad_object=JugadorPais.objects.filter(pais=ipais['pais'])
        lista_jugad_array=[]
        for ijugador in lista_jugad_object:
            lista_jugad_array.append(ijugador.nombre)
        pais_jugadordict[cont]={ipais['pais']:lista_jugad_array}
        cont+=1
    return JsonResponse(pais_jugadordict)
#
def estadopago(rsala,rgrupo,ruser):
    estado=PagoSalaEquipoIdeal.objects.get(nombreJuego=rsala,grupo=rgrupo,user=ruser).estadopago
    return estado

def grupoexiste(nombre):
    existe=''
    cant=salaequipoideal.objects.filter(nombreJuego=nombre).count()
    if cant>=1:
        existe='El nombre de la sala ya existe'
    return (existe)
#
def getSalasdeGrupoEI(rgrupos):
    rpta=[]
    #'sala-grupo'
    for j in rgrupos:
        salas=salaequipoideal.objects.filter(grupo=j,estado='activo')
        for i in salas:
            dato=i.nombreJuego+'-'+j
            rpta.append(dato)
    return rpta
#
def GenerarPago(sala,pago,grupo):
    rsala=sala;rgrupo=grupo;
    usuarios=Invitacion.objects.filter(grupo=rgrupo,estado='aceptado')
    print ('cant'+str(usuarios.count()))
    for i in usuarios:
        gpago=PagoSalaEquipoIdeal(nombreJuego=rsala,grupo=rgrupo,estadopago='deuda',user=i.invitado)
        print ('creadndo pago sala'+ rsala+"-Grupo"+rgrupo+"-usuario"+i.invitado)
        gpago.save()
    return None
