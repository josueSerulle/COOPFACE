from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.

def index(request):
    return render(request, "landingPage/base.html")

def sendMailView(request):
    if request.method == "POST":
        subject         = 'Contacto'
        from_email      = settings.DEFAULT_FROM_EMAIL   
        message         = 'COOPFACE'
        recipient_list  = [request.POST['email']]           
        html_message    = "<h3>Gracias por contactarse " + request.POST['name'] + ' ' + request.POST['surname'] + ' nos pondremos en contacto los mas pronto psoible.'
        
        send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message)
        
        subject         = 'Contacto ' + request.POST['name'] + ' ' + request.POST['surname']
        from_email      = settings.DEFAULT_FROM_EMAIL   
        message         = 'Contacto Cliente'
        recipient_list  = [settings.DEFAULT_FROM_EMAIL ]           
        html_message    = "<h3>" + request.POST['name'] + ' ' + request.POST['surname'] +  "de correo " +  request.POST['email'] + " realizo el siguiente comentario: " + request.POST['comentario']
        
        send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message)
    
    return redirect("index")