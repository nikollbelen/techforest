from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Planes)
admin.site.register(Pagos)
admin.site.register(Profile)
admin.site.register(Errores)
admin.site.register(Dispositivos)
admin.site.register(Opciones)
admin.site.register(Valvula)