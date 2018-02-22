from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
from polla.models import Partido,Apuestas
from users.models import usuariocuenta
from django.contrib.auth.models import User
from django.db.models import F

# Create your views here.
def construccion(request):
    pass


def templatepolla(request):
    context={
    'usuario':request.user.username
    }
    return render(request,'partidos.html',context)

def templatepollaApostar(request):
    context={
    'usuario':request.user.username
    }
    return render(request,'partidosApostar.html',context)

def obtenerPartidos(request):
    jsonrespuesta={}
    listaPartidos= Partido.objects.all()
    partidos_serialized = serializers.serialize('json', listaPartidos)
    return JsonResponse(partidos_serialized, safe=False)

def updatePartido(request):
    jsonrespuesta={}
    idpartido = request.POST.get('idpartido')
    ganador = request.POST.get('ganador')
    partido = Partido.objects.get(pk=idpartido)
    partido.estado = True
    #partido.estado = False
    partido.save()
    apuestas = Apuestas.objects.filter(partido=partido, pronostico=ganador)
    for apu in apuestas:
        usuario = usuariocuenta.objects.filter(usuario=apu.user.username).update(dinerocuenta=F('dinerocuenta')+apu.ganancia)

    return JsonResponse(jsonrespuesta)


def saveApuesta(request):
    jsonrespuesta={}
    idpartido = request.POST.get('idpartido')
    monto = request.POST.get('monto')
    ganancia = request.POST.get('ganancia')
    pronostico = request.POST.get('pronostico')
    partido = Partido.objects.get(pk=idpartido)
    user = User.objects.get(username=request.user.username)
    apuesta = Apuestas(partido= partido, monto=monto, ganancia=ganancia, pronostico=pronostico, user=user)
    usuariocuenta.objects.filter(usuario=request.user.username).update(dinerocuenta=F('dinerocuenta')-monto)
    apuesta.save()


    return JsonResponse(jsonrespuesta)
