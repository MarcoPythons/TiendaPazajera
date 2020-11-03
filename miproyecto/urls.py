"""miproyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views 
from registros import Rviews
from productos import Pviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.pag_inicial, name='pag_principal'),
    path('registro/', Rviews.registro_usuario, name='registro_usuario'),
   # path('User-Created/', Rviews.registrado, name='registrado'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('Gestion-productos/', Pviews.registro_producto, name ='registro_productos'),
    path('listar-productos/', Pviews.listar_productos, name ='listar_productos'),
    path('listar-productos/resultado-filtro/', Pviews.filtro, name ='resultado_filtro'),
    path('Modificar-productos/resultado-filtro/<id>/', Pviews.filtrador_modificar, name ='modificar'),
    path('Eliminar-productos/resultado-filtro/<id>/', Pviews.eliminar_producto, name ='eliminar'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
