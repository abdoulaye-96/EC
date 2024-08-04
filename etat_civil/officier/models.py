"""
models of the officier app.
"""
import datetime
from django.db import models

class Declaration(models.Model):
    numDecl = models.CharField(max_length=50)
    annDecl = models.PositiveIntegerField()
    jourDecl = models.PositiveIntegerField()
    moisDecl = models.PositiveIntegerField()
    heurDecl = models.DateField()
    langDecl = models.CharField(max_length=255)
    lieDecl = models.CharField(max_length=255)

    def __str__(self):
        return self.numDecl

class Declarant(models.Model):
    idD = models.AutoField(primary_key=True)
    nomD = models.CharField(max_length=100)
    prenomD = models.CharField(max_length=100, default='John')
    lieNceD = models.CharField(max_length=155)
    datNceD = models.DateTimeField(auto_now_add=False, blank=True)
    profD = models.CharField(max_length=255)
    qualiteD = models.CharField(max_length=100)
    adresD = models.CharField(max_length=255)
    declaration = models.ForeignKey(Declaration, on_delete=models.CASCADE, related_name='declarants')

    def __str__(self):
        return self.nomD

class Enfant(models.Model):
    nomEnf = models.CharField(max_length=100)
    dateNceEnf = models.DateField(default=datetime.datetime.now)
    heureNceEnf = models.TimeField()
    lieNceEnf = models.CharField(max_length=255)
    sexNceEnf = models.CharField(max_length=255)
    numero = models.IntegerField()
    declaration = models.ForeignKey(Declaration, on_delete=models.CASCADE, related_name='enfants')

    def __str__(self):
        return self.nomEnf

class Pere(models.Model):
    idP = models.AutoField(primary_key=True)
    nomP = models.CharField(max_length=100)
    prenomP = models.CharField(max_length=100, default='John')
    adresP = models.CharField(max_length=255)
    lieNceP = models.CharField(max_length=100)
    datNceP = models.DateTimeField(auto_now_add=False, blank=True)
    profP = models.CharField(max_length=255)
    natP = models.CharField(max_length=255)
    declaration = models.ForeignKey(Declaration, on_delete=models.CASCADE, related_name='peres')

    def __str__(self):
        return self.nomP

class Mere(models.Model):
    idM = models.AutoField(primary_key=True)
    nomM = models.CharField(max_length=100)
    prenomM = models.CharField(max_length=100, default='John')
    adresM = models.CharField(max_length=255)
    lieNceM = models.CharField(max_length=100)
    datNceM = models.DateTimeField(auto_now_add=False, blank=True)
    profM = models.CharField(max_length=255)
    natM = models.CharField(max_length=255)
    declaration = models.ForeignKey(Declaration, on_delete=models.CASCADE, related_name='meres')

    def __str__(self):
        return self.nomM
