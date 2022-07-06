from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from coopVirtual.backEnds.AuthBackEnd import AuthBackend
from coopVirtual.models.UsersModel import UserForm

# Create your views here.

def loginForm(request):
    return render(request, "coopVirtual/auth/login.html");

def login(request):
    print("hola")
    auth = AuthBackend()
    
    if request.method == "POST":
        formValid = UserForm(request.POST)
        
        if formValid.is_valid():
            if auth.authenticate(request = request, username= formValid.cleaned_data["username"], password = formValid.cleaned_data["password"]):
                return JsonResponse({},safe = False)
            
    return JsonResponse({"error": ""}, safe = False, status = 400)

