from django.shortcuts import render
from .models import JugadorPais
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from django.core import serializers
from django.http import JsonResponse


# Create your views here.
def JuegoEquipoIdeal(request):
    context={
    'usuario':request.user.username
    }
    return render(request,'jugar.html',context)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def retornarjugadores(request):
    if request.method == 'GET':
        datos = JugadorPais.objects.all()
        return JsonResponse(datos,safe=False)
