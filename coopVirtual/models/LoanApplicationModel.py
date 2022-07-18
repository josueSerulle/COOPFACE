from django.db import models
from coopVirtual.models.LoanTypeModel import LoanTypeModel
from coopVirtual.models.PersonModel import PersonModel
from django import forms
# Create your models here.

class LoanApplicationModel(models.Model):
    id_socio            = models.ForeignKey(PersonModel, on_delete = models.CASCADE, related_name = 'FK_loanApplication_partner',   null = True) 
    id_garannte         = models.ForeignKey(PersonModel, on_delete = models.CASCADE, related_name = 'FK_loanApplication_guarantor', null = True)
    id_familia          = models.ForeignKey(PersonModel, on_delete = models.CASCADE, related_name = 'FK_loanApplication_family',    null = True)
    parentesco          = models.CharField(max_length = 50, null = True)
    id_tipo_prestamo    = models.ForeignKey(LoanTypeModel,  on_delete = models.CASCADE, null = True)
    fecha_solicitud     = models.DateField(null = True)
    monto_solicitado    = models.DecimalField(null = True, max_digits = 19, decimal_places = 2)
    cuotas              = models.IntegerField(null = True)
    observacion         = models.TextField(null = True)
    estado              = models.IntegerField(default = 1)
    
class LoanApplicationForm(forms.Form):
    tipo_prestamo   = forms.IntegerField(required = True)
    monto           = forms.CharField(required = True)
    cuotas          = forms.IntegerField(required = True)