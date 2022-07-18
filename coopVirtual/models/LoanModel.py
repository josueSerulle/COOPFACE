from django.db import models
from coopVirtual.models.LoanTypeModel import LoanTypeModel
from coopVirtual.models.PersonModel import PersonModel
from coopVirtual.models.UsersModel import UsersModel
from coopVirtual.models.LoanApplicationModel import LoanApplicationModel

# Create your models here.

class LoanModel(models.Model):
    id_socio            = models.ForeignKey(PersonModel,            on_delete = models.CASCADE, related_name = 'FK_loan_partner', null = True) 
    id_solicitud        = models.ForeignKey(LoanApplicationModel,   on_delete = models.CASCADE, null = True)
    id_garannte         = models.ForeignKey(PersonModel,            on_delete = models.CASCADE, related_name = 'FK_loan_guarantor', null = True)
    id_usuario          = models.ForeignKey(UsersModel,             on_delete = models.CASCADE, null = True)
    id_tipo_prestamo    = models.ForeignKey(LoanTypeModel,          on_delete = models.CASCADE, null = True)
    fecha_prestamo      = models.DateField(null = True)
    fecha_vencimiento   = models.DateField(null = True)
    monto_prestamo      = models.DecimalField(null = True, max_digits = 19, decimal_places = 2)
    cuotas              = models.IntegerField(null = True)
    interes             = models.DecimalField(null = True, max_digits = 19, decimal_places = 2)
    observacion         = models.TextField(null = True)
    estado              = models.IntegerField(default = 1)