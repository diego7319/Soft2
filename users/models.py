from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class Usuario(models.Model):
    user = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.user
