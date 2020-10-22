
from django.urls import path, include
from . import views


urlpatterns = [
    path('registro_completo', views.registro_completo, name='registro_completo')
]