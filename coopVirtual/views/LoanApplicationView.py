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
from coopVirtual.backends.SavingTransactionBackEnd import SavingTransactionBackEnd
from coopVirtual.decorators import partner_required
from coopVirtual.models.LoanApplicationModel import LoanApplicationForm, LoanApplicationModel



# Create your views here.

@login_required(login_url='login')
@partner_required
def indexView(request):
    return render(request, "coopVirtual/loandApplication/index.html")

@login_required(login_url='login')
@partner_required
def  datatable(request):
    data            = []
    loanApplication = LoandApplicationBackEnd()
    
    for list in loanApplication.loandApplicationList():
        data.append({
            "id"                : list.id,
            "tipoPrestamo"      : list.id_tipo_prestamo.descripcion,
            "fechaSolicitud"    : list.fecha_solicitud,
            "cuotas"            : list.cuotas,
            "monto"             : list.monto_solicitado,
            "estado"            : list.estado
        })
    
    return JsonResponse({"data": data}, safe = False)

@login_required(login_url='login')
@partner_required
def createView(request):
    loanApplication = LoandApplicationBackEnd()
    
    return render(request, "coopVirtual/loandApplication/create.html", {"loandTypes": loanApplication.getAllLoandType()})

@login_required(login_url='login')
@partner_required
def insertView(request):
    
    if request.method == "POST":
        
        if int(request.POST['tipo_prestamo']) == 1:
            return loanGerencial(request)
        elif int(request.POST['tipo_prestamo']) == 2:
            return loanExpreso(request)

def loanGerencial(request):
    loanApplication = LoandApplicationBackEnd()
    user            = UserBackEnd()
    formValidate    = LoanApplicationForm(request.POST)
    
    if formValidate.is_valid():
        loanApplicationModel = LoanApplicationModel()
        
        
        loanApplicationModel.id_socio            = user.getPerson(request.user.persona_id)
        loanApplicationModel.id_tipo_prestamo    = loanApplication.getLoanType(formValidate.cleaned_data['tipo_prestamo'])
        loanApplicationModel.fecha_solicitud     = datetime.now()
        loanApplicationModel.monto_solicitado    = formValidate.cleaned_data['monto'].replace("$","").replace(",","")
        loanApplicationModel.cuotas              = formValidate.cleaned_data['cuotas']
        loanApplicationModel.estado              = 1
        
        loanApplicationModel.save()
        
        sendMail(request)
        return redirect('loand_application')
        
    messages.error(request, formValidate.errors)
    return redirect("loand_application_create")

def loanExpreso(request):
    loanApplication     = LoandApplicationBackEnd()
    user                = UserBackEnd()
    savingTransaction   = SavingTransactionBackEnd()
    formValidate        = LoanApplicationForm(request.POST)
    
    
    if formValidate.is_valid():
        locale.setlocale(locale.LC_ALL, 'en_US')
        savingNormalTotal   = savingTransaction.savingNormalTotal()
        monto               = float(formValidate.cleaned_data['monto'].replace("$","").replace(",",""))
        print(savingNormalTotal)
        if(monto > savingNormalTotal):
            messages.error(request, "El monto seleccionado " + formValidate.cleaned_data['monto']  + " es mayor a su total de ahorro normal $ " + f'{round(savingNormalTotal, 2):,}')
            return redirect("loand_application_create")
        
        loanApplicationModel = LoanApplicationModel()
        
        loanApplicationModel.id_socio            = user.getPerson(request.user.persona_id)
        loanApplicationModel.id_tipo_prestamo    = loanApplication.getLoanType(formValidate.cleaned_data['tipo_prestamo'])
        loanApplicationModel.fecha_solicitud     = datetime.now()
        loanApplicationModel.monto_solicitado    = formValidate.cleaned_data['monto'].replace("$","").replace(",","")
        loanApplicationModel.cuotas              = formValidate.cleaned_data['cuotas']
        loanApplicationModel.estado              = 1
        
        loanApplicationModel.save()
        
        sendMail(request)
        return redirect('loand_application')
        
    
    messages.error(request, formValidate.errors)
    return redirect("loand_application_create")

def sendMail(request):
    subject = 'Solicitud de préstamo Recibida'
    from_email = settings.DEFAULT_FROM_EMAIL   
    message = 'prestamo COOPFACE'
    recipient_list = [request.user.persona.correo]           
    html_message = render_to_string("coopVirtual/emailTemplate/template.html", {"message": "por esta vía le informamos que su solicitud de préstamos fue recibida y por la misma se la estará notificando el proceso."}, request = request)
    send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message)
    
    messages.success(request, 'Solicitud creada exitosamente!')