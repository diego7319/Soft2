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
from .models import notificacionesEI,Pozo_salaEI,scoreEI,salaEI,PagoSalaEI,ScorejuegoEI

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


def iniciarjuegopracticaEIdeal(request):

    #cantpreg=salatrivia.objects.get(nombreJuego=nombrejuego,grupo=grupo).cantpreguntas
    context={
    'cantpreg':10,
    'user':request.user.username
    }
    return render(request,'equipoidealpractica.html',context)

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













def score(request):
    if not request.user.is_authenticated:
        return redirect('index')
    respuesta=request.POST.get('respuesta')
    pregunta=request.POST.get('pregunta')
    objpregunta=PreguntaTrivia.objects.get(descPregunta=pregunta)
    jsonrespuesta={'resultado':'Respuesta incorrecta'}
    if objpregunta.respuesta==respuesta:
        rpuntaje='1'
        jsonrespuesta['resultado']='Respuesta correcta'

    return JsonResponse(jsonrespuesta)

def crearjuego(request):
    if not request.user.is_authenticated:
        return redirect('index')
    else:
        info=request.POST
        estado='activo'
        nombresala=info.get('nombresala')
        nombregrupo=info.get('grupo')
        cantpreg=int(info.get('cantpreg'))
        rpago=int(info.get('pago'))
        rusuario=info.get('usuario')
        nombreusado={}
        if grupoexiste(nombresala)=='El nombre de la sala ya existe':
            nombreusado['existe']='El nombre de la sala ya existe,use otro nombre'
            nombreusado['misgrupos']=useradmingroup(request.user.username)
            nombreusado['usuario']=request.user.username
            print ("EXISTE")
            return JsonResponse({'rpta':'Sala ya existe'})
        else:
            salaobj=salatrivia(nombreJuego=nombresala,grupo=nombregrupo,cantpreguntas=cantpreg,
            estado='activo',pago=rpago);
            salaobj.save();
            Pozo_sala(nombreJuego=nombresala,dinero=0).save();
            GenerarPago(nombresala,rpago,nombregrupo);
            print ("CREADO")
            return JsonResponse({'existe':'Sala de juego creada'})

def guardarscore(request):
    rsala=request.POST.get('sala')
    rusuario=request.POST.get('usuario')
    rgrupo=request.POST.get('grupo')
    rresultado=request.POST.get('resultado')
    if (Scorejuego.objects.filter(nombreJuego=rsala,grupo=rgrupo,user=rusuario).count()>=1):
        return JsonResponse({"rpta":"Ya haz jugado esta sala"})
    else:
        d=Scorejuego(nombreJuego=rsala,grupo=rgrupo,user=rusuario,resultado=rresultado)
        d.save()
#return JsonResponse({'rpta':'error en guardar score'})
        return JsonResponse({'rpta':'Guardado correctamente'})

def templatetrivia(request):
    context={
    'misgrupos':useradmingroup(request.user.username),
    'usuario':request.user.username,
        }
    return render(request,'configurartrivia.html',context)

def Admin_calcularganador(request):
    rsala=request.POST.get("sala")
    sala_vacia=desactivarsala(rsala)
    if sala_vacia==None:
        context={
        'existe':'No hubo juegos en la sala',
        'misgrupos':useradmingroup(request.user.username),
        'usuario':request.user.username
        }
        return HttpResponse("asd")
    else:
        winers,losers=calculo_ganador_perdedor(rsala)
        monto=calcular_pozo_sala(rsala,winers)
        notificacionganadores(winers,monto,rsala)
        notificacionperdedores(losers,rsala)
        return HttpResponse("<script>window.location.href = window.location.href;</script>")


def iniciarjuego(request):
    info=request.POST
    usuario=info['jugarusuario']
    nombrejuego=info['jugarsala']
    grupo=info['jugargrupo']
    cantpreg=salatrivia.objects.get(nombreJuego=nombrejuego,grupo=grupo).cantpreguntas
    context={
    'cantpreg':cantpreg,
    'salatrivia':nombrejuego,
    'user':usuario,
    'grupo':grupo
    }
    return render(request,'holi.html',context)

def iniciarjuegopracticatrivia(request):

    #cantpreg=salatrivia.objects.get(nombreJuego=nombrejuego,grupo=grupo).cantpreguntas
    context={
    'cantpreg':10,
    'user':request.user.username
    }
    return render(request,'juegopractica.html',context)

def pagar_sala(request):
    info=request.POST
    rusuario=info['jugarusuario']
    rnombrejuego=info['jugarsala']
    rgrupo=info['jugargrupo']
    cantpagar=salatrivia.objects.get(nombreJuego=rnombrejuego,grupo=rgrupo).pago
    saldouser=usuariocuenta.objects.get(usuario=rusuario)
    if int(cantpagar) > int(saldouser.dinerocuenta):
        return JsonResponse({"rpta": "No hay saldo suficiente en tu cuenta"})
    else:
        nuevosaldouser=saldouser.dinerocuenta-cantpagar
        cambiarestado=PagoSala.objects.get(nombreJuego=rnombrejuego,grupo=rgrupo,user=rusuario)
        saldouser.dinerocuenta=nuevosaldouser
        saldouser.save()
        agregar_dinero_Pozo(rnombrejuego,cantpagar)
        cambiarestado.estadopago='pagado'
        cambiarestado.save()
        return JsonResponse({"rpta": "Pago realizado"})



def obtenerSalas(request):
    jsonrespuesta={}
    ruser=request.POST.get('usuario')
    listagrupos=misgrupos(ruser)
    salagrupo= getSalasdeGrupo(listagrupos)
    cont=0
    for i in salagrupo:
        jsonrespuesta[str(cont)]={'sala':i.split('-')[0],'grupo':i.split('-')[1],'estado':estadopago(i.split('-')[0],i.split('-')[1],ruser)}
        cont+=1
    return JsonResponse(jsonrespuesta)


#devuelve las salas donde es administrador
def obtenerSalasadmin(request):
    jsonrespuesta={}
    ruser=request.POST.get('usuario')
    listagrupos=useradmingroup(ruser)
    salagrupo= getSalasdeGrupo(listagrupos)
    cont=0
    for i in salagrupo:
        jsonrespuesta[str(cont)]={'sala':i.split('-')[0],'grupo':i.split('-')[1]}
        cont+=1

    return JsonResponse(jsonrespuesta)

#funciones de apoyo
def grupoexiste(nombre):
    existe=''
    cant=salatrivia.objects.filter(nombreJuego=nombre).count()
    if cant>=1:
        existe='El nombre de la sala ya existe'
    return (existe)

def getSalasdeGrupo(rgrupos):
    rpta=[]
    #'sala-grupo'
    for j in rgrupos:
        salas=salatrivia.objects.filter(grupo=j,estado='activo')
        for i in salas:
            dato=i.nombreJuego+'-'+j
            rpta.append(dato)
    return rpta

#genera los pedidos de pago al usuario al crear una sala
def GenerarPago(sala,pago,rgrupo):
    rsala=sala;
    usuarios=Invitacion.objects.filter(grupo=rgrupo,estado='aceptado')
    for i in usuarios:
        print ("generando pago a "+i.invitado)
        gpago=PagoSala(nombreJuego=rsala,grupo=rgrupo,estadopago='deuda',user=i.invitado)
        gpago.save()

def calculo_ganador_perdedor(rsala):
    ganadores=[];perdedores=[]
    puntajeganador=0
    puntajes=[]
    jugadas=Scorejuego.objects.filter(nombreJuego=rsala)
    for juego in jugadas:
        puntajes.append(juego.resultado)
    puntajeganador= max(puntajes)
    for usuario in jugadas:
        if usuario.resultado==puntajeganador:
            ganadores.append(usuario.user)
        else:
            perdedores.append(usuario.user)
    return ganadores,perdedores

def estadopago(rsala,rgrupo,ruser):
    estado=PagoSala.objects.get(nombreJuego=rsala,grupo=rgrupo,user=ruser).estadopago
    return estado

def calcular_pozo_sala(sala,ganadores):
    monto=Pozo_sala.objects.get(nombreJuego=sala).dinero
    return (monto/len(ganadores))

def notificacionganadores(ganadores,monto,rsala):
    for i in ganadores:
        notif=notificaciones(user=i,ganador="si",sala=rsala)
        print ("notificacion win SI"+i )
        notif.save()
        recargar(i,monto)

def notificacionperdedores(perdedores,rsala):
    for i in perdedores:
        notif=notificaciones(user=i,ganador="no",sala=rsala)
        print ("notificacion win NO"+i )
        notif.save()

def desactivarsala(sala):
    print ("Nombre sala: %s" %(sala))
    objsala=salatrivia.objects.get(nombreJuego=sala)
    scorsala=Scorejuego.objects.filter(nombreJuego=sala)
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

def agregar_dinero_Pozo(rsala,rdinero):
    obj=Pozo_sala.objects.get(nombreJuego=rsala)
    obj.dinero=obj.dinero+rdinero
    obj.save()
