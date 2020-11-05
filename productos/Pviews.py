from django.shortcuts import render, redirect, get_object_or_404
from productos.models import Producto
from productos.forms import ProductoForm
from django.contrib.auth import login , authenticate
from miproyecto import views
from django.contrib.auth.decorators import login_required, permission_required




@permission_required('core.add_producto')
def registro_producto(request):

    data = {
        'form':ProductoForm
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Producto Guardado Correctamente"
        data['form']= formulario

    

    return render(request, "pagina-registro-productos.html", data)

@permission_required('core.view_producto')
def listar_productos(request):


    productos = Producto.objects.filter(id__exact =10)
    data = {

        'productos':productos
    }

    return render(request, "pagina-registro-productos.html", data)

@permission_required('core.view_producto')
def filtro(request):

    filtro_prenda = request.POST['filtro_prenda']

    if 'filtro_precio' in request.POST:
        filtro_precio = request.POST['filtro_precio']
    else:
        filtro_precio = ""

    if filtro_prenda != "":
        filtro = Producto.objects.filter(tipo_prenda__exact= filtro_prenda)
        data = {
        'productos':filtro
        }
        return render(request, "pagina-registro-productos.html", data)
    elif filtro_precio != "":
        precio_numero = int(filtro_precio)
        filtro2 = Producto.objects.filter(precio__exact= precio_numero)
        data = {
        'productos':filtro2
        }
        return render(request, "pagina-registro-productos.html", data)

@permission_required('core.change_producto')
def filtrador_modificar(request, id):    
    filtro_prenda = get_object_or_404(Producto, id=id)
    
    data = {
        'form':ProductoForm(instance=filtro_prenda)
        }
    if request.method == 'POST':
        formulario = ProductoForm(data= request.POST, instance=filtro_prenda)
        if formulario.is_valid():
            formulario.save()
            data['form'] = formulario

    return render(request, "modificar.html",data)

@permission_required('core.change_producto')
def eliminar_producto(request, id):
    filtro_prenda = get_object_or_404(Producto, id=id)
    filtro_prenda.delete()
    return redirect(to = "registro_productos")




    