from django.urls import path

from . import views

urlpatterns = [
    path('usuario',views.usuario_list),
    path('usuario/<int:pk>',views.usuario_detail),
    path('planes',views.planes_list),
    path('planes/<int:pk>',views.planes_detail),
    path('pagos',views.pagos_list),
    path('pagos/<int:pk>',views.pagos_detail),
    path('error',views.error_list),
    path('error/<int:pk>',views.error_detail),
    path('dispositivo',views.dispositivos_list),
    path('dispositivo/<int:pk>',views.dispositivos_detail),
    path('valvula',views.valvula_list),
    path('valvula/<int:pk>',views.valvula_detail),
    path('opciones',views.opciones_list),
    path('opciones/<int:pk>',views.opciones_detail),

    # Jose
    path('dispositivos/<int:pk>',views.dispositivos_detail),
    path('opciones/dispositivo/<int:pk>',views.opciones_dispositivo_detail),
    path('valvula/dispositivo/<int:pk>',views.valvula_dispositivo_detail),
    path('usuario/correo/<str:pk>',views.usuario_correo_detail),
    path('dispositivos/usuario/<int:pk>',views.dispositivo_usuario_detail)
]