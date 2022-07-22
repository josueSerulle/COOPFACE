from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..decorators import employee_required

# Create your views here.
@login_required(redirect_field_name= 'admin/login', login_url='login_admin')
@employee_required
def index(request):
    return render(request, "admin/home.html")