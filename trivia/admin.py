from django.contrib import admin
from .models import PreguntaTrivia
from django.contrib import admin
# Register your models here.


class PreguntaTriviaAdmin(admin.ModelAdmin):
    list_display = ('idPregunta','descPregunta','respuesta')
admin.site.register(PreguntaTrivia,PreguntaTriviaAdmin)
