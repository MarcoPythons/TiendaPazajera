from django.shortcuts import render, redirect , HttpResponse
from registros.models import usuario
from registros.forms import ClienteForm
from django.contrib.auth import login , authenticate
from miproyecto import views


#from django.contrib.auth.decorators import login_required  <--- este import se hace para poder usar el @login_required para que solo los que esten logeados puedan ver una vista


def registro_usuario(request):
    data = {
        'form':ClienteForm
    }

    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        email_form= request.POST['email']
        email_bd = usuario.objects.filter(email__exact = email_form)
        if email_bd:
            return HttpResponse("Este email ya se encuentra registrado!")
        else:
            if formulario.is_valid():
                formulario.save()
                username = formulario.cleaned_data['username']
                password = formulario.cleaned_data['password2']
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect(to='/home/')


    return render(request, "registration/registar.html", data)




#def registrado(request):

   # rut_desde_html =request.POST["rut"]
    
    #run_desde_bd=usuario.objects.filter(run__exact = rut_desde_html)

   # if run_desde_bd:
     #   return render(request, "registro_completo.html",{"rut_cliente":run_desde_bd, "query":rut_desde_html})

    #else:
    #    nombre_html = request.POST["nombre"]
     #   apellido_html = request.POST["apellido"]
    #    fecha_nacimiento = request.POST["fecNac"]
    #    correo_html = request.POST["correo"]
     #   password_html = request.POST["contra"]
     #  id_1 = random.randint(1, 100000000000000000)
       # cliente = Cliente(id_1 ,rut_desde_html,nombre_html, apellido_html, fecha_nacimiento, correo_html ,password_html)
      #  cliente.save()
      #  return render(request, "registro_completo.html",{"rut_cliente":run_desde_bd, "query":rut_desde_html})
    

    




    
