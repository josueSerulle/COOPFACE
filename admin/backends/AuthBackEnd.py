from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import login, logout
from coopVirtual.models.UsersModel import UsersModel

class AuthBackend(ModelBackend):
    
    def authenticate(self, request, username = None, password = None, **kwargs):
        try:
            user = UsersModel.objects.get(username = username)
            if user.check_password(password):
                login(request, user, backend= "admin.backends.AuthBackend")
                return user
        except UsersModel.DoesNotExist:
            return None
    
    def logout(self, request):
        return logout(request)