from django.contrib import admin
from .models import grupo
# Register your models here.
class GruposAdmin(admin.ModelAdmin):
    list_display = ('nombre','owner')
admin.site.register(grupo,GruposAdmin)
