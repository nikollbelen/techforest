from django.db import models
from django.contrib.auth.models import User

# Usuarios.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    correo = models.EmailField()
    imagen_perfil = models.ImageField(upload_to='usuarios',blank=True,null=True)

    def __str__(self):
        return self.nombres

# Opciones

class Planes(models.Model):
    DOMESTICO = 'domestico'
    EMPRESARIAL = 'empresarial'

    PLANES_CHOICES = (
        (DOMESTICO, 'Domestico'),
        (EMPRESARIAL, 'Empresarial'),
    )

    plan = models.CharField(max_length=200, default="0")
    tipo = models.CharField(max_length=100, choices=PLANES_CHOICES)
    usuarios = models.OneToOneField(User, on_delete=models.CASCADE, default="0")

    def __str__(self):
        return self.plan

class Pagos(models.Model):
    boleta = models.CharField(max_length=100, unique=True)
    costo = models.FloatField()
    fecha_pago = models.DateTimeField()
    planes = models.ForeignKey(Planes, on_delete=models.CASCADE)

    def __str__(self):
        return self.boleta

class Errores(models.Model):
    titulo = models.CharField(max_length=100)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now=True)
    usuarios = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Dispositivos(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    fecha_adquisicion = models.DateTimeField()
    imagen = models.ImageField(upload_to='diapositivos',blank=True,null=True)
    usuarios = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Valvula(models.Model):
    class Estados(models.IntegerChoices):
        Activo = 1
        Inactivo = 2

    estado = models.IntegerField(choices=Estados.choices)
    diapositivos = models.OneToOneField(Dispositivos, on_delete=models.CASCADE)

class Opciones(models.Model):
    valor_maximo = models.IntegerField()
    valor_minimo = models.IntegerField()
    humedad = models.IntegerField() 
    diapositivos = models.OneToOneField(Dispositivos, on_delete=models.CASCADE)

