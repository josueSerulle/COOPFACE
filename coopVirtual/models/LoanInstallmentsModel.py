from django.db import models

from coopVirtual.models.LoanModel import LoanModel

# Create your models here.

class LoanInstallmentsModel(models.Model):
    id_prestamo         = models.ForeignKey(LoanModel, on_delete = models.CASCADE)
    fecha_expiracion    = models.DateField(null = True)
    no_cuota            = models.IntegerField(null = True)
    capital             = models.DecimalField(null = True, max_digits = 19, decimal_places = 2)
    interes             = models.DecimalField(null = True, max_digits = 19, decimal_places = 2)
    atraso              = models.DecimalField(null = True, max_digits = 19, decimal_places = 2)
    pago_capital        = models.DecimalField(null = True, max_digits = 19, decimal_places = 2)
    pago_interes        = models.DecimalField(null = True, max_digits = 19, decimal_places = 2)
    pago_atraso         = models.DecimalField(null = True, max_digits = 19, decimal_places = 2)
    descuento           = models.DecimalField(null = True, max_digits = 19, decimal_places = 2)
    estado              = models.IntegerField(default = 1)