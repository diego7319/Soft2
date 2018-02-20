from django.contrib import admin
from .models import JugadorPais

# Register your models here.
class jugpaisadmin(admin.ModelAdmin):
    list_display = ('nombre','pais')
admin.site.register(JugadorPais,jugpaisadmin)
