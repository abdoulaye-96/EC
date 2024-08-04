"""
 forms of the officier app.
"""
from django import forms
from .models import Declarant, Enfant, Pere, Mere

class DeclarantForm(forms.ModelForm):
    class Meta:
        model = Declarant
        fields = ['nomD', 'prenomD', 'lieNceD', 'datNceD', 'profD']
        widgets = {
            'nomD': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nom'}),
            'prenomD': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nom'}),
            'lieNceD': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nom'}),
            'datNceD': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'nom'}),
            'profD': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'profession'}),
        }

class EnfantForm(forms.ModelForm):
    class Meta:
        model = Enfant
        fields = ['nomEnf', 'dateNceEnf', 'heureNceEnf', 'lieNceEnf', 'sexNceEnf', 'numero']
        widgets = {
            'nomEnf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nom'}),
            'dateNceEnf': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'nom'}),
            'heureNceEnf': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control', 'placeholder': 'heure'}),
            'lieNceEnf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nom'}),
            'sexNceEnf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'sexe'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'numero'}),
        }

class PereForm(forms.ModelForm):
    class Meta:
        model = Pere
        fields = ['nomP', 'prenomP', 'adresP', 'lieNceP', 'datNceP', 'profP']
        widgets = {
            'nomP': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'prenomP': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'adresP': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse'}),
            'lieNceP': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lieu de naissance'}),
            'datNceP': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Date de naissance'}),
            'profP': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Profession'}),
        }

class MereForm(forms.ModelForm):
    class Meta:
        model = Mere
        fields = ['nomM', 'prenomM', 'adresM', 'lieNceM', 'datNceM', 'profM']
        widgets = {
            'nomM': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nom'}),
            'prenomM': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'prenom'}),
            'adresM': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'adresse'}),
            'lieNceM': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'lieu'}),
            'datNceM': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'date'}),
            'profM': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'profession'}),
        }
