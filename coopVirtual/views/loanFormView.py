from datetime import datetime
import locale
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from coopVirtual.backends.LoandApplicationBackEnd import LoandApplicationBackEnd
from coopVirtual.backends.UserBackEnd import UserBackEnd
from coopVirtual.decorators import partner_required

@login_required(login_url='login_coop')
@partner_required
def loanFormView(request, loanApplicationId):
    user            = UserBackEnd()
    loan            = LoandApplicationBackEnd()
    person          = user.getPerson(request.user.persona_id) 
    personJob       = user.getJob(request.user.persona_id, True)
    personAddress   = user.getAddress(request.user.persona_id, True)
    loanApplcation  = loan.getLoanApplication(loanApplicationId)
    
    return render(request, "coopVirtual/loandApplication/loanForm.html", {"person" : person, "job" : personJob, "address" : personAddress, "loan": loanApplcation})

@login_required(login_url='login_coop')
@partner_required
def personView(request, cedula):
    user = UserBackEnd()
    person = user.getPersonByCedula(cedula)
    return JsonResponse({"person": list(person)}, safe = False)

@login_required(login_url='login_coop')
@partner_required
def insertView(request, loanApplicationId):
    garanteId = 0
    familarId = 0
    
    user            = UserBackEnd()
    loanApplication = LoandApplicationBackEnd()
    
    person = user.getPerson(request.user.persona_id)
            
    person.celular  = request.POST['userCelular']
    person.telefono = request.POST['userTelefono']
    person.correo   = request.POST['userCorreo']
    person.save()
    
    personJob = user.getJob(request.user.persona_id)
    
    personJob.empresa       = request.POST['userEmpresa']
    personJob.telefono      = request.POST['userEmpTelefono']
    personJob.sueldo        = request.POST['userSueldo'].replace("$","").replace(",","")
    personJob.id_persona_id = request.user.persona_id
    personJob.save()
        
    personAdrres = user.getAddress(request.user.persona_id)

    personAdrres.descripcion    = request.POST['userDireccion']
    personAdrres.id_persona_id  = request.user.persona_id
    personAdrres.save()
    
    for key, data in enumerate(request.POST.getlist('cedula[]'), 0):
        cedula = data.replace('-','').replace('-','')
        
        person = user.getPersonByDocument(cedula)
        
        person.cedula               = cedula
        person.nombre               = request.POST.getlist('nombre[]')[key]
        person.apellidos            = request.POST.getlist('apellido[]')[key]
        person.correo               = request.POST.getlist('correo[]')[key]
        person.celular              = request.POST.getlist('celular[]')[key]
        person.telefono             = request.POST.getlist('telefono[]')[key]
        person.id_tipo_persona_id   = 1
        
        person.save()
        
        if key == 0:
            garanteId = person.id
        else:
            familarId = person.id
    
        loan = loanApplication.getLoanApplication(loanApplicationId)
        
        loan.id_familia_id  = user.getPerson(familarId)
        loan.parentesco     = request.POST['parentesco']
        loan.id_garannte_id = user.getPerson(garanteId)
        loan.estado         = 1
        loan.save()
    
    sendMail(request)
    return redirect('loand_application')

def sendMail(request):
    subject = 'Solicitud de préstamo Recibida'
    from_email = settings.DEFAULT_FROM_EMAIL   
    message = 'prestamo COOPFACE'
    recipient_list = [request.user.persona.correo]           
    html_message = render_to_string("coopVirtual/emailTemplate/template.html", {"message": "por esta vía le informamos que su solicitud de préstamos fue recibida y por la misma se la estará notificando el proceso."}, request = request)
    send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message)
    
    messages.success(request, 'Solicitud creada exitosamente!')