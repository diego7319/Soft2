from django.shortcuts import render

# Create your views here.
def templateEquipoIdeal(request):
    context={
    'misgrupos':useradmingroup(request.user.username),
    'usuario':request.user.username
    }
    return render(request,'configurarjuego.html',context)
