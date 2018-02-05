from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from trivia.models import PreguntaTrivia
from random import randint,shuffle

# Create your views here.
def trivia(request):
    context = {
        'listapreguntas': preguntas
    }
    return render(request, 'main.html')#, context)

def score(request):
    acum = 0
    for x in preguntas():
        if x['opciones'][x['respuesta']] == request.POST.get(x['id'],''):
            acum += 100
    return render(request, 'score.html', {'score':acum})


def preguntas():
    preguntas = [
        {
            'id':'Pregunta1',
            'descripcion':'Primer mundial',
            'opciones':['0','1','2','3','4'],
            'respuesta':1
        },
        {
            'id':'Pregunta2',
            'descripcion':'Segundo mundial',
            'opciones':['5','6','7','8'],
            'respuesta':0
        }
    ]
    return preguntas


def templated(request):
    return render(request,'holi.html')

def mostrarpregunta(request):
    username = request.GET.get('username', None)
    cantidad = PreguntaTrivia.objects.count()

    pregjson={}

    pregunta=PreguntaTrivia.objects.filter(idPregunta=0)#randint(0, cantidad))
    #pregjson se retorna al html
    pregjson['pregunta']=pregunta.descPregunta,
    alternativasrandom=[pregunta.incorrecta1,pregunta.incorrecta2,
    pregunta.incorrecta3,pregunta.respuesta]
    alternativasrandom=shuffle(alternativasrandom)
    for i in alternativasrandom:
        tmp=d+str(i)
        pregjson[tmp]=alternativasrandom[i]
    return JsonResponse(pregjson)

def respuestapregunta(request):
    respuesta=request.POST
    pass
