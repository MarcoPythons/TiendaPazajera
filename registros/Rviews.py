from django.shortcuts import render
from registros.models import Cliente
import random



def ingresar(request):
    return render(request, "ingresar.html")

def registro(request):
    return render(request, "registar.html")


def registrado(request):

    rut_desde_html =request.POST["rut"]
    
    run_desde_bd=Cliente.objects.filter(run__exact = rut_desde_html)

    if run_desde_bd:
        return render(request, "registro_completo.html",{"rut_cliente":run_desde_bd, "query":rut_desde_html})

    else:
        nombre_html = request.POST["nombre"]
        apellido_html = request.POST["apellido"]
        fecha_nacimiento = request.POST["fecNac"]
        correo_html = request.POST["correo"]
        password_html = request.POST["contra"]
        id_1 = random.randint(1, 100000000000000000)
        cliente = Cliente(id_1 ,rut_desde_html,nombre_html, apellido_html, fecha_nacimiento, correo_html ,password_html)
        cliente.save()
        return render(request, "registro_completo.html",{"rut_cliente":run_desde_bd, "query":rut_desde_html})
    

    




    
