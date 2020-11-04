from django.contrib import admin
from productos.models import Producto 
# Register your models here.


#class PedidosAdmin(admin.ModelAdmin):
 #   list_display = ('numero_pedido',)
  #  search_fields = ('fecha_pedido',)


admin.site.register(Producto)

#admin.site.register(Pedido,PedidosAdmin)