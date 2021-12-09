from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [

    # Pagina principal
    path('', views.index, name='index'),
    path('planes', views.planes, name='planes'),
    path('soluciones', views.soluciones, name='soluciones'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('contacto', views.contacto, name='contacto'),
    path('login', views.login, name='login'),
    path('registroProfile', views.registroProfile, name='registroProfile'),
    path('registroPlan', views.registroPlan, name='registroPlan'),
    path('pago', views.pago, name='pago'),
    

    # Dashboard Cliente
    path('cliente/<int:cliente_id>', views.cliente, name='cliente'),
    path('cliente/<int:cliente_id>/perfil', views.perfilCliente, name='perfilCliente'),
    path('cliente/<int:cliente_id>/plan', views.planCliente, name='planCliente'),
    path('cliente/<int:cliente_id>/solucion', views.solucionCliente, name='solucionCliente'),
    path('cliente/<int:cliente_id>/dispositivo', views.dispositivoCliente, name='dispositivoCliente'),
    path('cliente/<int:cliente_id>/reportar', views.reportarCliente, name='reportarCliente'),
    path('cliente/<int:cliente_id>/reportes', views.reportesCliente, name='reportesCliente'),

    # Dashboard Administrador
    path('administrador/dashboard', views.admin_dashboard, name='dashboard'),
    path('administrador/administradores', views.administradores, name='administradores'),
    path('administrador/ayuda', views.ayuda, name='ayuda'),
    path('administrador/dispositivos', views.dispositivos, name='ayuda'),
    path('administrador/usuarios', views.usuarios, name='usuarios'),

    path('login-usuarios/', views.loginUser, name='loginpage'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.registerUser, name='register'),

]