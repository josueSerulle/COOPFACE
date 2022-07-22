
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from coopVirtual.backends.UserBackEnd import UserBackEnd
from coopVirtual.models.PersonModel import PersonForm
from ..decorators import partner_required
from django.contrib import messages

# Create your views here.

@login_required(login_url='login')
@partner_required
def editView(request):
    user            = UserBackEnd()
    person          = user.getPerson(request.user.persona_id) 
    personJob       = user.getJob(request.user.persona_id, True)
    personAddress   = user.getAddress(request.user.persona_id, True)
    
    return render(request, "coopVirtual/users/edit.html", {"person" : person, "job" : personJob, "address" : personAddress})

@login_required(login_url='login')
@partner_required
def updateView(request):
    user = UserBackEnd()
    
    if request.method == "POST":
        formValid = PersonForm(request.POST)
        
        if formValid.is_valid():
            person = user.getPerson(request.user.persona_id)
            
            person.celular  = formValid.cleaned_data['celular']
            person.telefono = formValid.cleaned_data['telefono']
            person.correo   = formValid.cleaned_data['correo']
            person.save()
            
            if(request.POST['empresa']):
                personJob = user.getJob(request.user.persona_id)
                
                personJob.empresa       = request.POST['empresa']
                personJob.telefono      = request.POST['empTelefono']
                personJob.sueldo        = request.POST['sueldo'].replace("$","").replace(",","") if request.POST['sueldo'] else 0
                personJob.direccion     = request.POST['empDireccion']
                personJob.estado        = 1
                personJob.id_persona_id = request.user.persona_id
                personJob.save()
                
            if(request.POST['direccion']):
                personAdrres = user.getAddress(request.user.persona_id)

                personAdrres.descripcion    = request.POST['direccion']
                personAdrres.estado         = 1
                personAdrres.id_persona_id  = request.user.persona_id
                personAdrres.save()
            
            messages.success(request, 'Perfil Actualizado')
            return redirect("profile")