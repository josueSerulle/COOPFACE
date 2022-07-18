from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..decorators import partner_required

# Create your views here.

@login_required(login_url='login')
@partner_required
def index(request):
    print(request.user.persona.imagen)
    return render(request, "coopVirtual/home.html");