from django.db import models
from coopVirtual.models.PersonModel import PersonModel

# Create your models here.

class PersonAddressModel(models.Model):
    id_persona  = models.ForeignKey(PersonModel, on_delete = models.CASCADE) 
    descripcion = models.CharField(max_length = 255)
    estado      = models.IntegerField(default = 1)