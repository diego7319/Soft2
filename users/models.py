from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Usuario(models.Model):
    user = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
"""
    class Meta:
        model = User
        fields = ('user','password' )
    def save(self,commit=True):
        obj = super(Usuario, self).save(commit=False)
        obj.user = user
        obj.password = password
        if commit:
            obj.save()
        return obj
    def __str__(self):
        return user
"""
