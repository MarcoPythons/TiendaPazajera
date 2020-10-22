from django.db import models

# Create your models here.

#class Cliente(models.Model):
 #   id = models.IntegerField(primary_key=True)
  #  run= models.CharField(max_length=30, null=False) # Asi se crean los atributos de tipo texto
  #  nombre= models.CharField(max_length=30, null=False) #asi se crean los atributos de tipo numerico
  #  apellido = models.CharField(max_length=30, null=False)
  #  fecha_nacimiento = models.DateField(null=False)
  #  email = models.EmailField() #esto sirve para que se intruduscan emails validos
   # contrasenia =models.CharField(max_length=30, null=False)


#class Producto(models.Model):
  #  id = models.IntegerField(primary_key=True)
   # tipo_prenda = models.CharField(max_length=20, null=False)
   # precio = models.IntegerField(null=False)
 #   imagen = models.ImageField(null=False)


#hay que registrar la app en el settings en el campo installed_apps

#para comprobar si la aplicacion esta bien debemos usar el siguiente comando en la consola cmd

#py manage.py check "nombre de la app"

# para hacer la bd y las tablas que estan en este archivo, hay que digitar en la consola el siguiente comando:

#py manage.py makemigrations

#para installar el modulo de mysql es el siguiente comando 

    #pip install pymysql