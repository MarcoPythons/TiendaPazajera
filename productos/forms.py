from django import forms 
from django.forms import ModelForm
from productos.models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProductoForm(forms.ModelForm):
    

    class Meta:
        model = Producto
        fields = ('nombre','tipo_prenda','descripcion','precio', 'imagen')
        labels= {
            'nombre':'Nombre Del producto',
            'descripcion':'Descripción del producto',
            'precio':'Precio del producto',
            'tipo_prenda':'Tipo de prenda'
        }
        widgets = {
            'tipo_prenda':forms.TextInput(
                attrs = {
                    'class':'controls',
                    'type':'text',
                    'name':'tipo_prenda',
                    'id':'nombreproducto'
                }

            ),
            'nombre': forms.TextInput(
                attrs = {
                    'class':'controls',
                    'type':'text',
                    'name':'nombreproducto',
                    'id':'nombreproducto'
                }
            ), 
            'descripcion':forms.Textarea(
                attrs = {
                    'class':'controls',
                    'type':'text',
                    'name':'nombreproducto',
                    'id':'nombreproducto'
                }
            ),
            'precio':forms.TextInput(
                attrs = {
                    'class':'controls',
                    'type':'text',
                    'name':'nombreproducto',
                    'id':'nombreproducto'
                }
            ),
        }