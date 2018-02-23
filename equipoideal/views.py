from django.shortcuts import render
from .models import JugadorPais
from random import randint
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from django.http import JsonResponse
import json
from grupos.views import misgrupos,useradmingroup
from .models import notificacionesEI,Pozo_salaEI,scoreEI,salaEI,PagoSalaEI,ScorejuegoEI
from users.models import usuariocuenta
from grupos.models import Invitacion

"""simula api --> la api que encontramos
no tiene los jugadores de seleccion de
los paises en el mundial """

#Api de jugadores
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def retornarjugadores(request):
    datos={}
    if request.method == 'GET':
        return jugador_paisToJson()

#Retorna interfaz juego
def templatjuego(request):
    if not request.user.is_authenticated:
        return redirect('index')
    else:
        context={'misgrupos':misgrupos(request.user.username)}
        return render(request,'jugar.html',context)

#Retorna interfaz de configuracion
def config_EI(request):
    context={
    'misgrupos':useradmingroup(request.user.username),
    'usuario':request.user.username,
        }
    return render(request,'configurarjuego.html',context)

#Retorna juego de juegopractica
def iniciarjuegopracticaEIdeal(request):
    #cantpreg=salatrivia.objects.get(nombreJuego=nombrejuego,grupo=grupo).cantpreguntas
    context={
    'user':request.user.username
    }
    return render(request,'equipoidealpractica.html',context)

def crearjuegosala(request):
    if not request.user.is_authenticated:
        return redirect('index')
    else:
        info=request.POST
        estado='activo'
        nombresala=info.get('nombresala')
        nombregrupo=info.get('grupo')
        rpago=int(info.get('pago'))
        rusuario=info.get('usuario')
        if grupoexiste(nombresala)=='El nombre de la sala ya existe':
            return JsonResponse({'rpta':'Sala ya existe'})
        else:
            salaobj=salaEI(nombreJuego=nombresala,grupo=nombregrupo,
            estado='activo',pago=rpago);
            salaobj.save();
            Pozo_salaEI(nombreJuego=nombresala,dinero=0).save();
            GenerarPago(nombresala,rpago,nombregrupo);
            print ("CREADO")
            return JsonResponse({'existe':'Sala de juego creada'})

#Simulacion de generar el puntaje de los jugadores
def guardarscore(request):
    rsala=request.POST.get('sala')
    rusuario=request.POST.get('usuario')
    rgrupo=request.POST.get('grupo')
    rresultado=randint(70,120)
    buscarscore=ScorejuegoEI.objects.filter(nombreJuego=rsala,grupo=rgrupo,user=rusuario)
    if (buscarscore.count()>=1):
        p="Ya haz jugado esta sala. Puntaje: "+str(buscarscore[0].resultado)
        return JsonResponse({"rpta":p,'t':'0'})
    else:
        d=ScorejuegoEI(nombreJuego=rsala,grupo=rgrupo,user=rusuario,resultado=rresultado)
        d.save()
        p='Tu puntaje es de '+str(rresultado)
        return JsonResponse({'rpta': p,'t':'1'})

#obtener salas para usuario
def obtenerSalasEI(request):
    print ("obtenersalas EI")
    jsonrespuesta={}
    ruser=request.POST.get('usuario')
    listagrupos=misgrupos(ruser)
    salagrupo= getSalasdeGrupo(listagrupos)
    cont=0
    print ("  -")
    print (listagrupos)
    print (ruser)
    print (salagrupo)
    print ("  -")
    for i in salagrupo:
        print (i)
        jsonrespuesta[str(cont)]={'sala':i.split('-')[0],'grupo':i.split('-')[1],'estado':estadopago(i.split('-')[0],i.split('-')[1],ruser)}
        cont+=1

    return JsonResponse(jsonrespuesta)

#devuelve las salas dodne eres administrador
def obtenerSalasEIadmin(request):
    jsonrespuesta={}
    ruser=request.POST.get('usuario')
    listagrupos=useradmingroup(ruser)
    salagrupo= getSalasdeGrupo(listagrupos)
    cont=0
    for i in salagrupo:
        jsonrespuesta[str(cont)]={'sala':i.split('-')[0],'grupo':i.split('-')[1]}
        cont+=1

    return JsonResponse(jsonrespuesta)

#Paga la sala (ajax)
def pagar_sala(request):
    info=request.POST
    rusuario=info['jugarusuario']
    rnombrejuego=info['jugarsala']
    rgrupo=info['jugargrupo']
    cantpagar=salaEI.objects.get(nombreJuego=rnombrejuego,grupo=rgrupo).pago
    saldouser=usuariocuenta.objects.get(usuario=rusuario)
    if int(cantpagar) > int(saldouser.dinerocuenta):
        return JsonResponse({"rpta": "No hay saldo suficiente en tu cuenta"})
    else:
        nuevosaldouser=saldouser.dinerocuenta-cantpagar
        cambiarestado=PagoSalaEI.objects.get(nombreJuego=rnombrejuego,grupo=rgrupo,user=rusuario)
        saldouser.dinerocuenta=nuevosaldouser
        saldouser.save()
        agregar_dinero_Pozo(rnombrejuego,cantpagar)
        cambiarestado.estadopago='pagado'
        cambiarestado.save()
        return JsonResponse({"rpta": "Pago realizado"})

#Inicia el juego equipo Ideal
def iniciarjuegoEI(request):
    info=request.POST
    usuario=info['jugarusuario']
    nombrejuego=info['jugarsala']
    grupo=info['jugargrupo']
    context={
    'salatrivia':nombrejuego,
    'user':usuario,
    'grupo':grupo
    }
    return render(request,'jugar.html',context)

def Admin_calcularganadorEI(request):
    rsala=request.POST.get("sala")
    sala_vacia=desactivarsala(rsala)
    if sala_vacia==None:
        """
        context={
        'existe':'No hubo juegos en la sala',
        'misgrupos':useradmingroup(request.user.username),
        'usuario':request.user.username
        }"""
        return JsonResponse({'rpta':'sala vacia'})
    else:
        winers,losers=calculo_ganador_perdedor(rsala)
        monto=calcular_pozo_sala(rsala,winers)
        notificacionganadores(winers,monto,rsala)
        notificacionperdedores(losers,rsala)
        return JsonResponse({'rpta':'se obtuvo ganador'})

"""
FUNCIONES DE SOPORTE
"""
#Convierte DB pais-Jugador a Json
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


#verifica si el nombre de la sala ya existe
def grupoexiste(nombre):
    existe=''
    cant=salaEI.objects.filter(nombreJuego=nombre).count()
    if cant>=1:
        existe='El nombre de la sala ya existe'
    return (existe)
#Genera la deuda a los miembros del grupo al crear una sala
def GenerarPago(sala,pago,rgrupo):
    rsala=sala;
    usuarios=Invitacion.objects.filter(grupo=rgrupo,estado='aceptado')
    for i in usuarios:
        gpago=PagoSalaEI(nombreJuego=rsala,grupo=rgrupo,estadopago='deuda',user=i.invitado)
        gpago.save()

#obtiene las salas del grupo del juego
def getSalasdeGrupo(rgrupos):
    rpta=[]
    #'sala-grupo'
    for j in rgrupos:
        salas=salaEI.objects.filter(grupo=j,estado='activo')
        for i in salas:
            print (i)
            dato=i.nombreJuego+'-'+j
            rpta.append(dato)
    return rpta
#verifica si un usuario ha pagado la sala
def estadopago(rsala,rgrupo,ruser):
    print ("Estado Pago:")
    print ("Sala:  "+rsala)
    print ("user:  "+ruser)
    print ("grupo:  "+rgrupo)
    print ((PagoSalaEI.objects.filter(user=ruser).count()))
    estado=PagoSalaEI.objects.get(nombreJuego=rsala,grupo=rgrupo,user=ruser).estadopago

    return estado

def agregar_dinero_Pozo(rsala,rdinero):
    obj=Pozo_salaEI.objects.get(nombreJuego=rsala)
    obj.dinero=obj.dinero+rdinero
    obj.save()


#Calcula el monto a dar al ganador(es)
def calcular_pozo_sala(sala,ganadores):
    monto=Pozo_salaEI.objects.get(nombreJuego=sala).dinero
    return (monto/len(ganadores))

def notificacionganadores(ganadores,monto,rsala):
    for i in ganadores:
        notif=notificacionesEI(user=i,ganador="si",sala=rsala)
        print ("notificacion win SI"+i )
        notif.save()
        recargar(i,monto)

def notificacionperdedores(perdedores,rsala):
    for i in perdedores:
        notif=notificacionesEI(user=i,ganador="no",sala=rsala)
        print ("notificacion win NO"+i )
        notif.save()

def calculo_ganador_perdedor(rsala):
    ganadores=[];perdedores=[]
    puntajeganador=0
    puntajes=[]
    jugadas=ScorejuegoEI.objects.filter(nombreJuego=rsala)
    for juego in jugadas:
        puntajes.append(juego.resultado)
    puntajeganador= max(puntajes)
    for usuario in jugadas:
        if usuario.resultado==puntajeganador:
            ganadores.append(usuario.user)
        else:
            perdedores.append(usuario.user)
    return ganadores,perdedores


def desactivarsala(sala):
    print ("Nombre sala: %s" %(sala))
    objsala=salaEI.objects.get(nombreJuego=sala)
    scorsala=ScorejuegoEI.objects.filter(nombreJuego=sala)
    if scorsala.count()==0:
        print ("count none")
        objsala.estado="desactivado"
        objsala.save()
        return None
    else:
        print ("count else")
        objsala.estado="desactivado"
        objsala.save()
        return "200"
