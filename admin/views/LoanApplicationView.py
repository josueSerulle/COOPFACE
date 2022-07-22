from datetime import datetime
import locale
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from admin.backends.LoandApplicationBackEnd import LoandApplicationBackEnd
from coopVirtual.backends.UserBackEnd import UserBackEnd
from admin.decorators import employee_required

# Create your views here.

@login_required(login_url='login_admin')
@employee_required
def indexView(request):
    return render(request, "admin/loandApplication/index.html")

@login_required(login_url='login_admin')
@employee_required
def  datatable(request):
    data            = []
    loanApplication = LoandApplicationBackEnd()
    
    for list in loanApplication.loandApplicationList():
        data.append({
            "id"                : list.id,
            "socio"             : list.id_socio.nombre + ' ' + list.id_socio.apellidos,
            "tipoPrestamo"      : list.id_tipo_prestamo.descripcion,
            "fechaSolicitud"    : list.fecha_solicitud,
            "cuotas"            : list.cuotas,
            "monto"             : list.monto_solicitado,
            "estado"            : list.estado
        })
    
    return JsonResponse({"data": data}, safe = False)

@login_required(login_url='login_admin')
@employee_required
def formView(request, loanApplicationId):
    user            = UserBackEnd()
    loan            = LoandApplicationBackEnd()
    loanApplcation  = loan.getLoanApplication(loanApplicationId)
    person          = user.getPerson(loanApplcation.id_socio_id) 
    personJob       = user.getJob(loanApplcation.id_socio_id, True)
    personAddress   = user.getAddress(loanApplcation.id_socio_id, True)
    socio           = user.getUser(loanApplcation.id_socio_id)
    
    return render(request, "admin/loandApplication/loanForm.html", {"person" : person, "job" : personJob, "address" : personAddress, "loan": loanApplcation, 'partner': socio})

@login_required(login_url='login_admin')
@employee_required
def insertView(request, loanApplicationId):
    if request.POST['estado-solicitud'] == request.POST['estado']:
        messages.error(request, 'Debe actualizar el estado de la solicitud!')
        return redirect("loan_form_admin", loanApplicationId=loanApplicationId)
    
    loan = LoandApplicationBackEnd()
    loanApplcation = loan.getLoanApplication(loanApplicationId)
    loanApplcation.estado       = request.POST['estado']
    loanApplcation.observacion  = request.POST['obseracion']
    loanApplcation.save()
    
    sendMail(request, loanApplcation)
    return redirect('loan_application_admin')

def sendMail(request, loandApplication):
    locale.setlocale(locale.LC_ALL, 'en_US')
    
    estado          = ["Recibido","Revisada","Aprobada","Declinada"]
    monto           = f'{round(loandApplication.monto_solicitado, 2):,}'
    messageMail     = "por esta vía le informamos que su solicitud de préstamos con un monte de $ " + monto +  " fue " + estado[int(loandApplication.estado) - 1] + "."
    subject         = 'Solicitud de préstamo Recibida'
    from_email      = settings.DEFAULT_FROM_EMAIL   
    message         = 'prestamo COOPFACE'
    recipient_list  = [loandApplication.id_socio.correo]           
    html_message    = render_to_string("admin/emailTemplate/template.html", {"message": messageMail, "observacion": loandApplication.observacion, "name": loandApplication.id_socio.nombre + ' ' + loandApplication.id_socio.apellidos}, request = request)
    
    send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message)
    
    messages.success(request, 'Solicitud editada exitosamente!')