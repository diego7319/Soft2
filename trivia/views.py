from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
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
