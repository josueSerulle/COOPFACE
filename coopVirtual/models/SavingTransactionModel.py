from django.db import models
from coopVirtual.models.PersonModel import PersonModel
from coopVirtual.models.SavingTypeModel import SavingTypeModel

# Create your models here.

class SavingTransactionModel(models.Model):
    id_socio            = models.ForeignKey(PersonModel, on_delete = models.CASCADE, null = True)
    id_tipo_ahorro      = models.ForeignKey(SavingTypeModel, on_delete = models.CASCADE, null = True)
    fecha               = models.DateField(null = True)
    monto               = models.DecimalField(null = True, max_digits=19, decimal_places=2)
    tipo_transaccion    = models.BooleanField(null = True)
    estado              = models.IntegerField(default = 1)