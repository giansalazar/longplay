from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser

# modelos relacionados con el administrador o admins.

class Personas(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    apep = models.CharField(max_length=30, verbose_name="Apellido Paterno")
    apem = models.CharField(max_length=30, verbose_name="Apellido Materno")
    genero = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre + self.apep
    
    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

#modelos relacionados a los discos

class Continentes(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Continente"
        verbose_name_plural = "Continentes"

class Paises(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    id_continente = models.ForeignKey(Continentes, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Paises"

class Generos(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Genero"
        verbose_name_plural = "Generos"

class Artistas(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    id_pais = models.ForeignKey(Paises, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Artista"
        verbose_name_plural = "Artistas"

class Albumes(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    id_artista = models.ForeignKey(Artistas, on_delete=models.CASCADE)
    id_genero = models.ForeignKey(Generos, on_delete=models.CASCADE)
    anio_publicacion = models.DateField()
    num_canciones = models.IntegerField(null=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albumes"

class Canciones(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    id_album = models.ForeignKey(Albumes, on_delete=models.CASCADE)
    duracion = models.IntegerField(null=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Cancion"
        verbose_name_plural = "Canciones"


class Discos(models.Model):
    id_album = models.ForeignKey(Albumes, on_delete=models.CASCADE)
    id_pais_fabricacion = models.ForeignKey(Paises, on_delete=models.CASCADE)
    edicion = models.CharField(max_length=30)
    condicion = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Disco"
        verbose_name_plural = "Discos"


#Tablas relacionados con los usuarios

class UsuarioManager(BaseUserManager):

    def _create_user(self, username, id_persona_id, telefono, email, is_active, is_staff, tipo_usuario, is_superuser, password):
        if not email:
            raise ValueError("El usuario debe tener un email")
        
        usuario = self.model(username=username, id_persona_id=id_persona_id, telefono=telefono, email=self.normalize_email(email), is_active=is_active, is_staff=is_staff, tipo_usuario=tipo_usuario, is_superuser=is_superuser)

        usuario.set_password(password)
        usuario.save(using=self.db)
        return usuario
    
    def create_user(self, username, id_persona_id, telefono, email, tipo_usuario, password=None):
        return self._create_user(username, id_persona_id, telefono, email, True, True, tipo_usuario, False, password)
    
    def create_superuser(self, username, id_persona_id, telefono, email, password):
        
        usuario=self.create_user(email,username=username, id_persona=id_persona_id, telefono=telefono, email=email, password=password)

        usuario.is_superuser=True

        usuario.save()

        return usuario
    

class Usuario(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(verbose_name="Usuario", max_length=20, unique=True)
    id_persona = models.ForeignKey(Personas, on_delete=models.CASCADE, verbose_name="Persona")
    telefono =  models.CharField(max_length=10, verbose_name="Télefono")
    email = models.EmailField(verbose_name="Email")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    tipo_usuario = models.CharField(max_length=25)
    objects=UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = 'telefono','email','id_persona'

class usuarios_codigos(models.Model):
    codigo_reg = models.CharField(max_length=10)
    id_persona = models.ForeignKey(Personas, on_delete=models.CASCADE)
    estatus_reg = models.IntegerField(null=True)
    tipo_usuario = models.CharField(max_length=20,null=True)


class Publicaciones(models.Model):
    id_disco = models.ForeignKey(Discos, on_delete = models.CASCADE)
    fecha_pub = models.DateTimeField(auto_now_add = True)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length = 240)
    id_usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)