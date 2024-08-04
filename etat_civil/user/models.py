"""
models of the user app.
"""
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    fonction = models.CharField(max_length=150)

    def __str__(self):
        return self.nom
