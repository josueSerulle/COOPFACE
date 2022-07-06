from django.shortcuts import render

# Create your views here.

def index(request):
    template = "coopVirtual/auth/login.html"
    if request.user.is_authenticated:
        template = "coopVirtual/home.html"
    
    return render(request, template);