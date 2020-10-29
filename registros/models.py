from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager




class UsuarioManager(BaseUserManager): #con esto se puede crear usuarios personalizados
    
    def create_user(self, email, username , run, nombre, apellido, fecha_nacimiento, password):   #asi creo un usuario normal
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico!')
        
        usuario = self.model(
            username = username, 
            email = self.normalize_email(email) ,#normalize_email es un validador de email
            run = run,
            nombre = nombre, 
            apellido = apellido,
            fecha_nacimiento = fecha_nacimiento
        ) 
        usuario.set_password(password) # asi encriptamos la contraseña 
        usuario.save()
        return usuario

    def create_superuser(self, username,email,run, nombre, apellido, fecha_nacimiento, password): # asi se crea un usuario administrador
        usuario = self.create_user(
            email,
            run = run,
            username = username, 
            nombre = nombre, 
            apellido = apellido,
            fecha_nacimiento = fecha_nacimiento,
            password = password
        )   

        usuario.usuario_administrador = True
        usuario.save()
        return usuario
    

class usuario(AbstractBaseUser): # usuario personalizado
    username = models.CharField(unique=True, max_length=30)
    run= models.CharField(max_length=30, null=False) # Asi se crean los atributos de tipo texto
    nombre= models.CharField(max_length=30, null=False) #asi se crean los atributos de tipo numerico
    apellido = models.CharField(max_length=30, null=False)
    fecha_nacimiento = models.DateField(null=False, verbose_name ="Fecha de nacimiento")
    email = models.EmailField(null=False) #esto sirve para que se intruduscan emails validos
    usuario_activo = models.BooleanField(default = True) #permisos de usuario normal
    usuario_administrador = models.BooleanField(default= False) #permisos de administrador
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['run', 'nombre', 'apellido', 'fecha_nacimiento', 'email'] 

    def __str__(self):
        return f'{self.username},{self.nombre}'

    def has_perm(self,perm,obj = None): #se debe crear este metodo para que el administrado de djnago pueda acceder al admin de djnago
        return True
    
    def has_module_perms(self,app_label): #este metodo sirve para usarse en el admin de django
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador
    
    class Meta:
        db_table = 'Usuarios' # para que la tabla se llame "Cliente" en la base de datos
        ordering = ['run'] # para ordenar por run
        #required_db_vendor = 'mysql' #esto es para dar a conocer con que base de datos trabaja



