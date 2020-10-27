from django.shortcuts import render
from registros.models import Cliente

def ingresar(request):
    return render(request, "ingresar.html")

def registro(request):
    return render(request, "registar.html")


def registrado(request):

    rut_desde_html =request.POST["rut"]

    run_desde_bd=Cliente.objects.filter(run__exact = rut_desde_html)

    return render(request, "registro_completo.html",{"rut_cliente":run_desde_bd, "query":rut_desde_html})




    
