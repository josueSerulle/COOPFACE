from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from coopVirtual.models.PersonModel import PersonModel
from django import forms

class UsersModel(AbstractBaseUser):
    persona     = models.OneToOneField(PersonModel, on_delete = models.CASCADE)
    is_partner  = models.BooleanField(default = False)
    is_employee = models.BooleanField(default = False)
    codigo      = models.CharField(null = True, max_length = 50, unique = True)
    username    = models.CharField(null = True, max_length = 50, unique = True)
    
    USERNAME_FIELD = 'username'

class UserForm(forms.Form):
    username = forms.CharField(max_length = 50, required = True)
    password = forms.CharField(required = True)