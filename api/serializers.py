from rest_framework import serializers
from .models import *

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id')

    def create(self, validated_data):
        """
        Create and return a new `Usuarios` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','user','nombres','apellidos','correo','imagen_perfil')

    def create(self, validated_data):
        """
        Create and return a new `Usuarios` instance, given the validated data.
        """
        return Profile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Usuarios` instance, given the validated data.
        """
        instance.user = validated_data.get('user', instance.user)
        instance.nombres = validated_data.get('nombres', instance.nombres)
        instance.apellidos = validated_data.get('apellidos', instance.apellidos)
        instance.correo = validated_data.get('correo', instance.correo)
        instance.imagen_perfil = validated_data.get('imagen_perfil', instance.imagen_perfil)
        instance.save()
        return instance

class PlanesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planes
        fields = ('id', 'plan', 'tipo', 'usuarios')

    def create(self, validated_data):
        """
        Create and return a new `Planes` instance, given the validated data.
        """
        return Planes.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Planes` instance, given the validated data.
        """
        instance.plan = validated_data.get('plan', instance.plan)
        instance.tipo = validated_data.get('tipo', instance.tipo)
        instance.usuarios = validated_data.get('usuarios', instance.usuarios)
        instance.save()
        return instance

class PagosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagos
        fields = ('id', 'boleta', 'costo', 'fecha_pago', 'planes')

    def create(self, validated_data):
        """
        Create and return a new `Pagos` instance, given the validated data.
        """
        return Pagos.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Pagos` instance, given the validated data.
        """
        instance.boleta = validated_data.get('boleta', instance.boleta)
        instance.costo = validated_data.get('costo', instance.costo)
        instance.fecha_pago = validated_data.get('fecha_pago', instance.fecha_pago)
        instance.planes = validated_data.get('planes', instance.planes)
        instance.save()
        return instance
    
class ErroresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Errores
        fields = ('id', 'titulo', 'mensaje', 'fecha_envio', 'usuarios')

    def create(self, validated_data):
        """
        Create and return a new `Errores` instance, given the validated data.
        """
        return Errores.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Errores` instance, given the validated data.
        """
        instance.titulo = validated_data.get('titulo', instance.titulo)
        instance.mensaje = validated_data.get('mensaje', instance.mensaje)
        instance.fecha_envio = validated_data.get('fecha_envio', instance.fecha_envio)
        instance.usuarios = validated_data.get('usuarios', instance.usuarios)
        instance.save()
        return instance

class DispositivosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivos
        fields = ('id', 'nombre', 'estado', 'fecha_adquisicion', 'imagen', 'usuarios')

    def create(self, validated_data):
        """
        Create and return a new `Diapositivos` instance, given the validated data.
        """
        return Dispositivos.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Diapositivos` instance, given the validated data.
        """
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.estado = validated_data.get('estado', instance.estado)
        instance.fecha_adquisicion = validated_data.get('fecha_adquisicion', instance.fecha_adquisicion)
        instance.imagen = validated_data.get('imagen', instance.imagen)
        instance.usuarios = validated_data.get('usuarios', instance.usuarios)
        instance.save()
        return instance

class ValvulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valvula
        fields = ('id', 'estado', 'diapositivos')

    def create(self, validated_data):
        """
        Create and return a new `Valvula` instance, given the validated data.
        """
        return Valvula.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Valvula` instance, given the validated data.
        """
        instance.estado = validated_data.get('estado', instance.estado)
        instance.diapositivos = validated_data.get('diapositivos', instance.diapositivos)
        instance.save()
        return instance

class OpcionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opciones
        fields = ('id', 'valor_maximo', 'valor_minimo', 'humedad','diapositivos')

    def create(self, validated_data):
        """
        Create and return a new `Opciones` instance, given the validated data.
        """
        return Opciones.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Opciones` instance, given the validated data.
        """
        instance.valor_maximo = validated_data.get('valor_maximo', instance.valor_maximo)
        instance.valor_minimo = validated_data.get('valor_minimo', instance.valor_minimo)
        instance.humedad = validated_data.get('humedad', instance.humedad)
        instance.diapositivos = validated_data.get('diapositivos', instance.diapositivos)
        instance.save()
        return instance
