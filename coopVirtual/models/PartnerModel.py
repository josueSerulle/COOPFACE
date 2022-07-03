from django.db import models
from coopVirtual.models.PersonModel import PersonModel

# Create your models here.

class PartnerModel(models.Model):
    id_persona  = models.ForeignKey(PersonModel, on_delete = models.CASCADE) 
    usuario     = models.CharField(max_length = 50)
    clave       = models.CharField(max_length = 50)
    estado      = models.IntegerField(default = 1)