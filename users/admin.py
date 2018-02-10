from django.contrib import admin
from .models import usuariocuenta
# Register your models here.
from django.contrib import admin

class usuariocuentaAdmin(admin.ModelAdmin):
    list_display = ('usuario','dinerocuenta')
admin.site.register(usuariocuenta,usuariocuentaAdmin)
