from django import forms
from django.forms import ModelForm
from registros.models import usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ClienteForm(ModelForm):

    class Meta:
        model = usuario
        fields = [  'username',
                    'password'
                    'run', 
                    'nombre',
                    'apellido',
                    'fecha_nacimiento',
                    'email',
                    ]


