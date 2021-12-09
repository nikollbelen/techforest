from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from api.models import *


class ErrorForm(forms.ModelForm):  
    class Meta:  
        model = Errores  
        fields = ["titulo","mensaje",]  


class UsuarioForm(forms.ModelForm):  
    class Meta:  
        model = Profile  
        fields = ["nombres","apellidos","correo","imagen_perfil"]  



class ProfileForm(forms.ModelForm):
    class Meta: 
        model = Profile  
        fields = "__all__"

class PlanForm(forms.ModelForm):
    class Meta: 
        model = Planes  
        fields = "__all__"


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Primer Nombre',
            'email': 'Correo Electronico',
            'username': 'Username',
            'password1': 'Clave',
            'password2': 'Confirmar clave'
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
