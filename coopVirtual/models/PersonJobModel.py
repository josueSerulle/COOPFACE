from django.db import models

from coopVirtual.models.PersonModel import PersonModel

# Create your models here.

class PersonJobModel(models.Model):
    id_persona  = models.ForeignKey(PersonModel, on_delete = models.CASCADE) 
    empresa     = models.CharField(max_length = 50)
    telefono    = models.CharField(max_length = 12)
    sueldo      = models.DecimalField(null = True, max_digits=19, decimal_places=2)
    direccion   = models.CharField(max_length = 255)
    estado      = models.IntegerField(default = 1)