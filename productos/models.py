from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=20, null=False)
    descripcion = models.CharField(max_length=30, verbose_name ="Descripción")
    precio = models.IntegerField()
    
    class Meta:
        db_table = 'Producto'
        required_db_vendor = 'mysql'
        ordering = ['precio']


    def __str__(self):
        return 'datos del producto %s , %s , %s' %  (self.nombre, self.descripcion, self.precio)

class Pedido(models.Model):
    numero_pedido = models.IntegerField(null = True)
    fecha_pedido = models.DateField('Fecha del pedido', auto_now=True, auto_now_add= False)
    entregado = models.BooleanField(default=False)
    id_Producto = models.ManyToManyField(Producto)
    

    class Meta:
        db_table = 'Pedido'
        ordering = ['fecha_pedido']
        required_db_vendor = 'mysql'



