from django.contrib import admin
from .models import JugadorPais,salaequipoideal,PagoSalaEquipoIdeal

# Register your models here.
class jugpaisadmin(admin.ModelAdmin):
    list_display = ('nombre','pais')
admin.site.register(JugadorPais,jugpaisadmin)


class salaequipoidealadmin(admin.ModelAdmin):
    list_display = ('nombreJuego','grupo','estado','pago','estado')
admin.site.register(salaequipoideal,salaequipoidealadmin)

class PagoSalaEquipoIdealadmin(admin.ModelAdmin):
    list_display = ('nombreJuego','grupo','estadopago','user')
admin.site.register(PagoSalaEquipoIdeal,PagoSalaEquipoIdealadmin)
