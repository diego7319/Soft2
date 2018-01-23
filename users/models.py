from django.db import models


class Usuario(models.Model):
    user = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

    def __str__(self):
        return user
