from django.shortcuts import render

# Create your views here.
def JuegoEquipoIdeal(request):
    context={
    'usuario':request.user.username
    }
    return render(request,'jugar.html',context)
