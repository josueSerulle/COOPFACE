from coopVirtual.models.PersonModel import PersonModel
from coopVirtual.models.PersonJobModel import PersonJobModel
from coopVirtual.models.PersonAddressModel import PersonAddressModel
from django.core.exceptions import ObjectDoesNotExist

class UserBackEnd:
    
    def getPerson(self, personId):
        try:
            person = PersonModel.objects.get(id=personId)
        except ObjectDoesNotExist:
            person = None
        
        return person
        
    def getJob(self, personId, isView = False):
        try:
            job = PersonJobModel.objects.get(id_persona_id=personId)
        except ObjectDoesNotExist:
            job = None if isView else PersonJobModel()
        
        return job
    
    def getAddress(self, personId, isView = False):
        try:
            address = PersonAddressModel.objects.get(id_persona_id=personId)
        except ObjectDoesNotExist:
            address = None if isView else PersonAddressModel()
        
        return address
    
    def getPersonByCedula(self, cedula):
        try:
            person = PersonModel.objects.filter(cedula=cedula).values()
        except ObjectDoesNotExist:
            person = {}
        
        return person
    
    def getPersonByDocument(self, cedula):
        try:
            person = PersonModel.objects.get(cedula=cedula)
        except ObjectDoesNotExist:
            person = PersonModel
        
        return person