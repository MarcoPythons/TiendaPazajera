from django.db import models





class Cliente(models.Model):
    run= models.CharField(max_length=30, null=False) # Asi se crean los atributos de tipo texto
    nombre= models.CharField(max_length=30, null=False) #asi se crean los atributos de tipo numerico
    apellido = models.CharField(max_length=30, null=False)
    fecha_nacimiento = models.DateField(null=False, verbose_name ="Fecha de nacimiento")
    email = models.EmailField(null=False) #esto sirve para que se intruduscan emails validos
    contrasenia =models.CharField(max_length=400, null=False, verbose_name ="Constraseña")

    class Meta:
        db_table = 'Cliente' # para que la tabla se llame "Cliente" en la base de datos
        ordering = ['run'] # para ordenar por run
        required_db_vendor = 'mysql' #esto es para dar a conocer con que base de datos trabaja

    def __str__ (self):
        return 'datos del cliente: %s , %s , %s, %s , %s' % (self.run, self.nombre, self.apellido, self.fecha_nacimiento, self.email)


    