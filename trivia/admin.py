from django.contrib import admin
from .models import PreguntaTrivia,salatrivia
from django.contrib import admin
# Register your models here.


class PreguntaTriviaAdmin(admin.ModelAdmin):
    list_display = ('idPregunta','descPregunta','respuesta')
admin.site.register(PreguntaTrivia,PreguntaTriviaAdmin)


class salatriviaadmin(admin.ModelAdmin):
    list_display = ('nombreJuego','grupo','estado','cantpreguntas')
admin.site.register(salatrivia,salatriviaadmin)
