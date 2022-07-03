from django.db import models

# Create your models here.

class SavingTypeModel(models.Model):
    descripcion = models.CharField(max_length = 50)
    estado      = models.IntegerField(default = 1)