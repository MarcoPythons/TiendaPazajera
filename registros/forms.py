from django import forms 
from django.forms import ModelForm
from registros.models import usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ClienteForm(forms.ModelForm):
    # Formulario de registro de un usuario en la base de datos

    password = forms.CharField(label = 'Contraseña',widget = forms.PasswordInput( #con widgets se pueden editar las etiquetas html que crea la api form

        attrs = {
            'class':'form-control',
            'id':'clave',
            'name':'password',
            'placeholder':'Ingresa tu contraseña',
            'required':'required'
        }))
    password2 = forms.CharField(label = 'Ingrese Contraseña Nuevamente',widget = forms.PasswordInput(

        attrs = {
            'class':'form-control',
            'id':'clave2',
            'name':'password2',
            'placeholder':'Repite tu contraseña',
            'required':'required'
        }
))

    class Meta:
        model = usuario
        fields = (  'username', 'run', 'nombre', 'apellido', 'fecha_nacimiento', 'email') #aca se pueden editar los tags html de los campos del modelo
        labels = {
            'username':'Nombre de usuario',
            'run':'Rut'
        }
        widgets = {
            'username': forms.TextInput (
                
            attrs ={
                'class': 'form-control',
                'id': 'username',
                'name': 'username',
                'placeholder': 'Ingresa un Nombre de usuario',
                'required':'required'
            }),
            'run': forms.TextInput(
            attrs = {
                'class': 'form-control',
                'required oninput': 'checkRut(this)',
                'id': 'rut',
                'placeholder': 'Ej: 12345678-k',
                'required maxlength': '10'
            }),
            'nombre': forms.TextInput(
            attrs = {
                'class': 'form-control',
                'id': 'nombre',
                'name': 'nombre',
                'placeholder': 'Ingresa tu nombre',
                'required':'required',
                'required maxlength': '30'
            }),
            'apellido': forms.TextInput(
                attrs= {
                'class': 'form-control',
                'id': 'apellido',
                'name': 'apellido',
                'placeholder': 'Ingresa tu apellido',
                'required':'required',
                'required maxlength': '30'  
                }),
            'fecha_nacimiento': forms.DateInput(
                attrs={
                'type': 'date',
                'class': 'form-control',
                'id': 'fecNac',
                'name': 'fecNac',
                'required':'required',
                'placeholder': 'Ejemplo: 1999-05-07',
                'min': '1930-01-01',
                'max': '2005-01-01'
                }),
            'email': forms.EmailInput(
                attrs= {
                'class': 'form-control',
                'id': 'correo',
                'name': 'correo',
                'required':'required',
                'placeholder': 'nombre@ejemplo.com'
                })
                }
    def clean_password(self): #aqui validamos la contraseña
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 !=password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2


    def save(self, commit = True): #aqui guardamos la contraseña cuando se valida
        user = super().save(commit = False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user


