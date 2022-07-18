from django.shortcuts import render, redirect
from coopVirtual.backends.AuthBackEnd import AuthBackend
from coopVirtual.models.UsersModel import UserForm

# Create your views here.

def loginView(request):
    auth = AuthBackend()
    if request.method == "POST":
        formValid = UserForm(request.POST)
        
        if formValid.is_valid():
            if auth.authenticate(request, username= formValid.cleaned_data["username"], password = formValid.cleaned_data["password"]):
                return redirect("coop_virtual")
        return render(request, "coopVirtual/auth/login.html", {"error": "Usuario o Contraseña incorrecta!!"});
    return render(request, "coopVirtual/auth/login.html");

def logoutView(request):
    auth = AuthBackend()
    auth.logout(request)
    return redirect("coop_virtual")