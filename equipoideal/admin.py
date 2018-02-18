from django.contrib import admin
from .models import JugadorPais,Partido

# Register your models here.
class jugpaisadmin(admin.ModelAdmin):
    list_display = ('nombre','pais')
admin.site.register(JugadorPais,jugpaisadmin)

class Partidoadmin(admin.ModelAdmin):
    list_dislay=('equipo1','equipo1','fecha','Grupo')
admin.site.register(Partido,Partidoadmin)
