from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader


def Pag_inicial(request):

   # pag_principal = loader.get_template('pag principal.html')
   # doc = pag_principal.render()
   # return HttpResponse (doc)
    return render(request , "pag principal.html")


def ingresar(request):
    return render(request, "ingresar.html")

def registro(request):
    return render(request, "registar.html")

def valida(request):
    user=request.GET['user']
    pwd=request.GET['pwd']

    user2 = user.strip(" ")
    
    if (user2 == 'duoc' and  pwd == 'duoc123'):
        return render(request, 'mensaje.html')
    else:
        return render(request, 'mensaje2.html', {'msg':'No valido'})