from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from trivia.models import PreguntaTrivia,scoretrivia,salatrivia
from random import randint,shuffle
from grupos.views import misgrupos
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
    rgrupo=request.POST.get('grupo')
    objpregunta=PreguntaTrivia.objects.get(descPregunta=pregunta)
    rpuntaje='0'
    jsonrespuesta={'resultado':'Respuesta incorrecta'}
    if objpregunta.respuesta==respuesta:
        print('CORRECTA')
        rpuntaje='1'
        jsonrespuesta['resultado']='Respuesta correcta'
    nuevoscore=scoretrivia(idpreguntaTrivia=objpregunta.idPregunta,
    user=request.user.username,puntaje=rpuntaje,grupo=rgrupo);
    nuevoscore.save()
    return JsonResponse(jsonrespuesta)

def crearjuego(request):
    if not request.user.is_authenticated:
        return redirect('index')

    else:

        request.Post
        context={'misgrupos':misgrupos(request.user.username)}
        return render(request,'holi.html',context)

def templatetrivia(request):
    context={
    'misgrupos':misgrupos(request.user.username)

    }
    return render(request,'configurartrivia.html',context)
