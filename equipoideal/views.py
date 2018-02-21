from django.shortcuts import render
from .models import JugadorPais
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from django.core import serializers
from django.http import JsonResponse
import json
from django.http import HttpResponse


# Create your views here.
def JuegoEquipoIdeal(request):
    context={
    'usuario':request.user.username
    }
    return render(request,'jugar.html',context)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def retornarjugadores(request):
    datos={}
    if request.method == 'GET':
        return jugador_paisToJson()




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
