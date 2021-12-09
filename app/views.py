from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from api.models import *
from .forms import *


# Pagina principal


def index(request):
    return render(request, 'principal/index.html', {})


def planes(request):
    return render(request, 'principal/planes.html', {})


def soluciones(request):
    return render(request, 'principal/soluciones.html', {})


def nosotros(request):
    return render(request, 'principal/about_us.html', {})


def contacto(request):
    return render(request, 'principal/contacto.html', {})


# def login(request):
#     form = LoginCliente(request.POST or None)
#     if form.is_valid():
#         user = form.save(commit=False)
#         correo = Profile.objects.get(correo=user.correo)
#         if user.contraseña == correo.contraseña:
#             return HttpResponseRedirect("/cliente/"+str(correo.user_id))
#         else:
#             return HttpResponseRedirect("")
#     return HttpResponseRedirect("")

def registroProfile(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/registroPlan")
    else:
        return render(request, 'principal/registroProfile.html', {'form':form})

def registroPlan(request):
    formPlan = PlanForm(request.POST or None)
    if formPlan.is_valid():
        formPlan.save()
        return HttpResponseRedirect("/pago")
    return render(request, 'principal/registroPlan.html', {'formPlan':formPlan})

def pago(request):
    return render(request, 'principal/pago.html', {})

# Dashboard Cliente
@login_required(login_url='/login-usuarios')
def cliente(request, cliente_id):
    cliente = get_object_or_404(Profile, user_id=cliente_id)
    plan = Planes.objects.get(usuarios_id=cliente_id)
    return render(request, 'cliente/index.html', {'cliente': cliente, 'plan': plan})


@login_required(login_url='/login-usuarios')
def perfilCliente(request, cliente_id):
    cliente = get_object_or_404(Profile, user_id=cliente_id)
    form = UsuarioForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/cliente/" + str(cliente_id) + "/perfil")

    return render(request, 'cliente/perfil.html', {'cliente': cliente, 'form': form})


@login_required(login_url='/login-usuarios')
def planCliente(request, cliente_id):
    cliente = get_object_or_404(Profile, user_id=cliente_id)
    plan = Planes.objects.get(usuarios_id=cliente_id)
    pagos = Pagos.objects.filter(planes_id=plan.id)
    return render(request, 'cliente/plan.html', {'cliente': cliente, 'plan': plan, 'pagos': pagos})


@login_required(login_url='/login-usuarios')
def solucionCliente(request, cliente_id):
    cliente = get_object_or_404(Profile, user_id=cliente_id)
    diapositivo = Dispositivos.objects.get(usuarios_id=cliente_id)
    opciones = Opciones.objects.get(diapositivos_id=diapositivo.id)
    return render(request, 'cliente/solucion.html', {'cliente': cliente, 'opciones': opciones})


@login_required(login_url='/login-usuarios')
def dispositivoCliente(request, cliente_id):
    cliente = get_object_or_404(Profile, user_id=cliente_id)
    dispositivo = Dispositivos.objects.get(usuarios_id=cliente_id)
    return render(request, 'cliente/dispositivo.html', {'cliente': cliente, 'dispositivo': dispositivo})


@login_required(login_url='/login-usuarios')
def reportarCliente(request, cliente_id):
    user = get_object_or_404(User, pk=cliente_id)
    cliente = get_object_or_404(Profile, user_id=cliente_id)
    form = ErrorForm(request.POST or None)
    if form.is_valid():
        error = form.save(commit=False)
        error.usuarios = user
        form.save()
        return HttpResponseRedirect("/cliente/" + str(cliente_id) + "/reportar")

    return render(request, 'cliente/reportar.html', {'cliente': cliente, 'form': form})


@login_required(login_url='/login-usuarios')
def reportesCliente(request, cliente_id):
    cliente = get_object_or_404(Profile, user_id=cliente_id)
    errores = Errores.objects.filter(usuarios_id=cliente_id)
    return render(request, 'cliente/reportes.html', {'cliente': cliente, 'errores': errores})


# Dashboard Administrador
def admin_dashboard(request):
    context = {}
    return render(request, 'administrador/admin_dashboard.html', context)


def administradores(request):
    context = {}
    return render(request, 'administrador/administradores.html', context)


def ayuda(request):
    context = {}
    return render(request, 'administrador/ayuda.html', context)


def dispositivos(request):
    context = {}
    return render(request, 'administrador/dispositivos.html', context)


def usuarios(request):
    context = {}
    return render(request, 'administrador/usuarios.html', context)

# Sesiones
def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'El usuario no existe')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/cliente/' + str(user.id))
        else:
            messages.error(request,'Usuario o clave incorrectos')

    return render(request, 'principal/login.html')


def logoutUser(request):
    logout(request)
    messages.info(request, 'Usuario ha salido del sistema')
    return redirect('/')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'La cuenta ha sido creada')

            login(request, user)
            return redirect('/registroProfile')

    else:
        messages.error(request, "Un error ha ocurrido durante el registro")

    context = {'page': page, 'form': form}
    return render(request, 'principal/register.html', context)
