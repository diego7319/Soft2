from django.contrib import admin
from .models import PreguntaTrivia,salatrivia,PagoSala,Scorejuego,Pozo_sala
from django.contrib import admin
# Register your models here.


class PreguntaTriviaAdmin(admin.ModelAdmin):
    list_display = ('idPregunta','descPregunta','respuesta')
admin.site.register(PreguntaTrivia,PreguntaTriviaAdmin)


class salatriviaadmin(admin.ModelAdmin):
    list_display = ('nombreJuego','grupo','estado','cantpreguntas','pago','estado')
admin.site.register(salatrivia,salatriviaadmin)

class PagoSaladmin(admin.ModelAdmin):
    list_display = ('nombreJuego','grupo','estadopago','user')
admin.site.register(PagoSala,PagoSaladmin)

class ScoreSaladmin(admin.ModelAdmin):
    list_display = ('user','grupo','nombreJuego','resultado')
admin.site.register(Scorejuego,ScoreSaladmin)

class Pozo_salaadmin(admin.ModelAdmin):
    list_display = ('nombreJuego','dinero')
admin.site.register(Pozo_sala,Pozo_salaadmin)
