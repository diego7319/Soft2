from django.contrib import admin
from .models import grupo,Invitacion
# Register your models here.
class GruposAdmin(admin.ModelAdmin):
    list_display = ('nombre','owner')
admin.site.register(grupo,GruposAdmin)

class InvitacionAdmin(admin.ModelAdmin):
    list_display = ('invitado','estado')
admin.site.register(Invitacion,InvitacionAdmin)
