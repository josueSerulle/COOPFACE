from django.contrib.auth.backends import ModelBackend
from coopVirtual.models.UsersModel import UsersModel

class AuthBackend(ModelBackend):
    
    def authenticate(self, request, username = None, password = None, **kwargs):
        try:
            user = UsersModel.objects.get(codigo = username)
            if user.check_password(password):
                return user
        except UsersModel.DoesNotExist:
            return None