from django.db import models


class Usuario(models.Model):
    email = models.CharField(max_length=10)
    password = models.CharField(max_length=10)


