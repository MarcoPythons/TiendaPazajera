from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=20, null=False)
    descripcion = models.CharField(max_length=30, verbose_name ="Descripción")
    precio = models.IntegerField()
    tipo_prenda = models.CharField(max_length=20, null=False)
    imagen = models.ImageField(null = True)
    
    
    class Meta:
        db_table = 'Producto'
        #required_db_vendor = 'mysql'
        ordering = ['precio']


    def __str__(self):
        return 'datos del producto %s , %s , %s' %  (self.nombre, self.descripcion, self.precio)




