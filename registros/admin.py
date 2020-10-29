from django.contrib import admin
from registros.models import usuario
# Register your models here.



class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "run" )
    search_fields= ("run",)
   #  con list_filter se puede hacer un filtro para hacer busquedas en las tablas


admin.site.register(usuario, ClientesAdmin)


