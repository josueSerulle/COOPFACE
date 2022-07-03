from django.db import models
from coopVirtual.models.PersonTypeModel import PersonTypeModel

# Create your models here.

class PersonModel(models.Model):
    id_tipo_persona = models.ForeignKey(PersonTypeModel, on_delete = models.CASCADE)
    nombre          = models.CharField(max_length = 50)
    apellidos       = models.CharField(max_length = 50)
    cedula          = models.CharField(max_length = 13)
    celular         = models.CharField(max_length = 11)
    telefono        = models.CharField(max_length = 11)
    correo          = models.CharField(max_length = 50)
    estado          = models.IntegerField(default = 1)