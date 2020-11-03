from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader
from productos.models import Producto
from productos.forms import ProductoForm


def pag_inicial(request):
    productos = Producto.objects.all()
    data= {

        'productos':productos
    }

   # pag_principal = loader.get_template('pag principal.html')
   # doc = pag_principal.render()
   # return HttpResponse (doc)
    return render(request , "pag principal.html", data)


def ingresar(request):
    return render(request, "ingresar.html")

def registro(request):
    return render(request, "registar.html")

