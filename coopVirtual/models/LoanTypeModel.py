from django.db import models

# Create your models here.

class LoanTypeModel(models.Model):
    descripcion     = models.CharField(max_length = 50)
    interes_mensual = models.DecimalField(null = True, max_digits=19, decimal_places=2)
    estado          = models.IntegerField(default = 1)