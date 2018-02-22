from django.contrib import admin
from .models import JugadorPais
from .models import notificacionesEI,salaEI,PagoSalaEI,ScorejuegoEI,Pozo_salaEI

# Register your models here.
class jugpaisadmin(admin.ModelAdmin):
    list_display = ('nombre','pais')
admin.site.register(JugadorPais,jugpaisadmin)

class salaEIadmin(admin.ModelAdmin):
    list_display = ('nombreJuego','grupo','estado','cantpreguntas','pago','estado')
admin.site.register(salaEI,salaEIadmin)

class PagoSaladmin(admin.ModelAdmin):
    list_display = ('nombreJuego','grupo','estadopago','user')
admin.site.register(PagoSalaEI,PagoSaladmin)

class ScoreSaladmin(admin.ModelAdmin):
    list_display = ('user','grupo','nombreJuego','resultado')
admin.site.register(ScorejuegoEI,ScoreSaladmin)

class Pozo_salaadmin(admin.ModelAdmin):
    list_display = ('nombreJuego','dinero')
admin.site.register(Pozo_salaEI,Pozo_salaadmin)

class notificacionesadmin(admin.ModelAdmin):
    list_display = ('user','ganador','estado','sala')
admin.site.register(notificacionesEI,notificacionesadmin)
