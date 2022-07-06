from django.db import models
from coopVirtual.models.LoanTypeModel import LoanTypeModel
from coopVirtual.models.PersonModel import PersonModel
from coopVirtual.models.UsersModel import UsersModel

# Create your models here.

class LoanApplicationModel(models.Model):
    id_socio            = models.ForeignKey(PersonModel,   on_delete = models.CASCADE, related_name = 'FK_loanApplication_partner') 
    id_garannte         = models.ForeignKey(PersonModel,    on_delete = models.CASCADE, related_name = 'FK_loanApplication_guarantor')
    id_tipo_prestamo    = models.ForeignKey(LoanTypeModel,  on_delete = models.CASCADE)
    fecha_solicitud     = models.DateField(null = True)
    monto_solicitado    = models.DecimalField(null = True, max_digits = 19, decimal_places = 2)
    cuotas              = models.IntegerField(null = True)
    observacion         = models.TextField(null = True)
    estado              = models.IntegerField(default = 1)