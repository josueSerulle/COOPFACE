from coopVirtual.models.LoanApplicationModel import LoanApplicationModel
from coopVirtual.models.LoanTypeModel import LoanTypeModel
from coopVirtual.models.UsersModel import UsersModel

class LoandApplicationBackEnd:
    
    def getLoanType(self, loadTypeId):
        return LoanTypeModel.objects.get(id = loadTypeId)
    
    def getAllLoandType(self):
        return LoanTypeModel.objects.all().filter(estado = 1)
    
    def loandApplicationList(selft):
        return LoanApplicationModel.objects.exclude(estado = 0).select_related("id_tipo_prestamo", "id_socio")
    
    def getLoanApplication(self, id):
        return LoanApplicationModel.objects.select_related("id_tipo_prestamo", "id_socio","id_familia", "id_garannte").get(id = id)