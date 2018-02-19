from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from users.models import usuariocuenta
from trivia.models import PreguntaTrivia,scoretrivia,salatrivia,PagoSala
from random import randint,shuffle,choice
from grupos.views import misgrupos,useradmingroup
from grupos.models import Invitacion
# Create your views here.
from rest_framework.decorators import api_view

def templated(request):
    if not request.user.is_authenticated:
        return redirect('index')
    else:
        context={'misgrupos':misgrupos(request.user.username)}
        return render(request,'holi.html',context)

def mostrarpregunta(request):
    if not request.user.is_authenticated:
        return redirect('index')
    username = request.POST.get('username', None)
    arreglousado=request.POST.get('usado')
    print (arreglousado)
    pregjson={}
    records = PreguntaTrivia.objects.all()
    #pregjson se retorna al html
    repetido=True
    while repetido==True:
        random_record = choice(records)
        print (arreglousado.split('-'))
        if str(random_record.idPregunta) in arreglousado.split('-'):
            repetido=True
        else:
            pregunta=random_record
            idp=random_record.idPregunta
            pregjson['pregunta']=pregunta.descPregunta,
            alternativasrandom=[pregunta.incorrecta1,pregunta.incorrecta2,
            pregunta.incorrecta3,pregunta.respuesta]
            shuffle(alternativasrandom)
            for i in range(0,4):
                tmp='d'+str(i)
                pregjson[tmp]=str(alternativasrandom[i])
                repetido=False
                pregjson['id']=idp

    return JsonResponse(pregjson)

#guarda la respuesta en la base de datos
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
        nombregrupo=info.get('grupo','')
        print (info.get('cantpreg'))
        cantpreg=int(info.get('cantpreg'))
        rpago=int(info.get('pago'))
        nombreusado={}
        if grupoexiste(nombresala)=='El nombre de la sala ya existe':
            nombreusado['existe']='El nombre de la sala ya existe,use otro nombre'
            nombreusado['misgrupos']=useradmingroup(request.user.username)
            nombreusado['usuario']=request.user.username
            return render(request,'configurartrivia.html',nombreusado)
        else:
            salaobj=salatrivia(nombreJuego=nombresala,grupo=nombregrupo,cantpreguntas=cantpreg,
            estado='activo',pago=rpago)
            salaobj.save()
            GenerarPago(nombresala,rpago,nombregrupo)
            context={'misgrupos':useradmingroup(request.user.username),
            'existe':'Sala de juego creada',
            'usuario':request.user.username
            }
            return render(request,'configurartrivia.html',context)


def templatetrivia(request):
    context={
    'misgrupos':useradmingroup(request.user.username),
    'usuario':request.user.username
    }
    return render(request,'configurartrivia.html',context)


def iniciarjuego(request):
    info=request.POST
    usuario=info['jugarusuario']
    nombrejuego=info['jugarsala']
    grupo=info['jugargrupo']
    cantpreg=salatrivia.objects.get(nombreJuego=nombrejuego,grupo=grupo).cantpreguntas
    context={
    'cantpreg':cantpreg,
    'salatrivia':nombrejuego,
    'user':usuario
    }
    return render(request,'holi.html',context)


def pagar_sala(request):
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
    listagrupos=misgrupos(ruser)
    salagrupo= getSalasdeGrupo(listagrupos)
    cont=0
    for i in salagrupo:
        jsonrespuesta[str(cont)]={'sala':i.split('-')[0],'grupo':i.split('-')[1],'estado':estadopago(i.split('-')[0],i.split('-')[1],ruser)}
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
def GenerarPago(sala,pago,grupo):
    rsala=sala;rgrupo=grupo;
    usuarios=Invitacion.objects.filter(grupo=rgrupo,estado='aceptado')
    print ('cant'+str(usuarios.count()))
    for i in usuarios:
        gpago=PagoSala(nombreJuego=rsala,grupo=rgrupo,estadopago='deuda',user=i.invitado)
        print ('creadndo pago sala'+ rsala+"-Grupo"+rgrupo+"-usuario"+i.invitado)
        gpago.save()
    return None
def MayorPuntaje(rsala,rgrupo):
    pass

def estadopago(rsala,rgrupo,ruser):
    estado=PagoSala.objects.get(nombreJuego=rsala,grupo=rgrupo,user=ruser).estadopago
    return estado
