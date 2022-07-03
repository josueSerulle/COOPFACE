from django.db import models
from coopVirtual.models.LoanTypeModel import LoanTypeModel
from coopVirtual.models.PartnerModel import PartnerModel
from coopVirtual.models.PersonModel import PersonModel
from coopVirtual.models.UsersModel import UsersModel

# Create your models here.

class LoanApplicationModel(models.Model):
    id_socio            = models.ForeignKey(PartnerModel,   on_delete = models.CASCADE) 
    id_garannte         = models.ForeignKey(PersonModel,    on_delete = models.CASCADE)
    id_usuario          = models.ForeignKey(UsersModel,     on_delete = models.CASCADE)
    id_tipo_prestamo    = models.ForeignKey(LoanTypeModel,  on_delete = models.CASCADE)
    fecha_solicitud     = models.DateField(null = True)
    monto_solicitado    = models.DecimalField(null = True, max_digits = 19, decimal_places = 2)
    cuotas              = models.IntegerField(null = True)
    observacion         = models.TextField(null = True)
    estado              = models.IntegerField(default = 1)