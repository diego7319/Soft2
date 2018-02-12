from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse

from trivia.models import PreguntaTrivia,scoretrivia,salatrivia,PagoSala
from random import randint,shuffle
from grupos.views import misgrupos,useradmingroup
# Create your views here.

def templated(request):
    if not request.user.is_authenticated:
        return redirect('index')
    else:
        context={'misgrupos':misgrupos(request.user.username)}
        return render(request,'holi.html',context)

def mostrarpregunta(request):
    if not request.user.is_authenticated:
        return redirect('index')
    username = request.GET.get('username', None)
    cantidad = PreguntaTrivia.objects.count()
    pregjson={}
    it=randint(1, cantidad)
    pregunta=PreguntaTrivia.objects.get(idPregunta=it)
    #pregjson se retorna al html
    print (pregunta.incorrecta1)
    pregjson['pregunta']=pregunta.descPregunta,
    alternativasrandom=[pregunta.incorrecta1,pregunta.incorrecta2,
    pregunta.incorrecta3,pregunta.respuesta]
    shuffle(alternativasrandom)
    for i in range(0,4):
        tmp='d'+str(i)
        pregjson[tmp]=str(alternativasrandom[i])
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
        print('CORRECTA')
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
            gpago=PagoSala(nombreJuego=nombresala,grupo=nombregrupo,estadopago='deuda',user=request.user.username)
            gpago.save()
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
    pass

def obtenerSalas(request):
    jsonrespuesta={}
    ruser=request.POST.get('usuario')
    listagrupos=misgrupos(ruser)
    salagrupo= getSalasdeGrupo(listagrupos)
    cont=0
    for i in salagrupo:
        jsonrespuesta[str(cont)]={i.split('-')[0]:i.split('-')[1]}
        cont+=1
    return JsonResponse(jsonrespuesta)
#devuelve las salas donde es administrador
def getsalasadmin(request):
    jsonrespuesta={}
    usuario=request.POST.get('usuario')
    useradmingroup()
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
        salas=salatrivia.objects.filter(grupo=j)
        for i in salas:
            dato=i.nombreJuego+'-'+j
            rpta.append(dato)
    return rpta
#genera los pedidos de pago al usuario al crear una sala
def GenerarPago(usuario,sala,pago,grupo):
    ruser=usuario;rsala=sala;rgrupo=grupo;
    gpago=PagoSala(nombreJuego=rsala,grupo=rgrupo,estadopago='deuda',user=ruser)
    try:
        gpago.save()
        return True
    except:
        return 'Error'

def MayorPuntaje(sala):
    pass
