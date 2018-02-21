from django.contrib import admin
from .models import Partido, Apuestas
# Register your models here.
class Partidoadmin(admin.ModelAdmin):
    list_dislay=('equipo1',)
admin.site.register(Partido,Partidoadmin)
admin.site.register(Apuestas,Partidoadmin)
