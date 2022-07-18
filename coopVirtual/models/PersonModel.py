from django.db import models
from django import forms
from coopVirtual.models.PersonTypeModel import PersonTypeModel

# Create your models here.

class PersonModel(models.Model):
    id_tipo_persona = models.ForeignKey(PersonTypeModel, on_delete = models.CASCADE, null = True)
    nombre          = models.CharField(max_length = 50)
    apellidos       = models.CharField(max_length = 50)
    cedula          = models.CharField(max_length = 50)
    celular         = models.CharField(max_length = 50)
    telefono        = models.CharField(max_length = 50)
    correo          = models.CharField(max_length = 50)
    imagen          = models.CharField(max_length = 50)
    estado          = models.IntegerField(default = 1)

class PersonForm(forms.Form):
    celular         = forms.CharField(required = True)
    telefono        = forms.CharField(required = True)
    correo          = forms.CharField(required = True)