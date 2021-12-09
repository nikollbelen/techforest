from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def usuario_list(request):
    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':
        usuario = Profile.objects.all()
        serializer = ProfileSerializer(usuario, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def usuario_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        usuario = Profile.objects.get(user_id=pk)
    except Profile.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProfileSerializer(usuario)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProfileSerializer(usuario, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        usuario.delete()
        return HttpResponse(status=204)
        
@csrf_exempt
def planes_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        planes = Planes.objects.get(pk=pk)
    except Planes.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PlanesSerializer(planes)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PlanesSerializer(planes, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        planes.delete()
        return HttpResponse(status=204)

@csrf_exempt
def planes_list(request):
    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':
        planes = Planes.objects.all()
        serializer = PlanesSerializer(planes, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PlanesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
        
@csrf_exempt
def pagos_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        pagos = Pagos.objects.get(pk=pk)
    except Pagos.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PagosSerializer(pagos)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PagosSerializer(pagos, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        pagos.delete()
        return HttpResponse(status=204)

@csrf_exempt
def pagos_list(request):
    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':
        pagos = Pagos.objects.all()
        serializer = PagosSerializer(pagos, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PagosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
        
@csrf_exempt
def error_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        error = Errores.objects.get(pk=pk)
    except Errores.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ErroresSerializer(error)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ErroresSerializer(error, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        error.delete()
        return HttpResponse(status=204)

@csrf_exempt
def error_list(request):
    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':
        error = Errores.objects.all()
        serializer = ErroresSerializer(error, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ErroresSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
        
@csrf_exempt
def dispositivos_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        diapositivos = Dispositivos.objects.get(pk=pk)
    except DispositivosSerializer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DispositivosSerializer(diapositivos)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DispositivosSerializer(diapositivos, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        diapositivos.delete()
        return HttpResponse(status=204)

@csrf_exempt
def dispositivos_list(request):
    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':
        diapositivos = Dispositivos.objects.all()
        serializer = DispositivosSerializer(diapositivos, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DispositivosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
        
@csrf_exempt
def valvula_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        valvula = Valvula.objects.get(pk=pk)
    except Valvula.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ValvulaSerializer(valvula)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ValvulaSerializer(valvula, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        valvula.delete()
        return HttpResponse(status=204)

@csrf_exempt
def valvula_diapositivos_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        valvula = Valvula.objects.get(pk=pk)
    except Valvula.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ValvulaSerializer(valvula)
        return JSONResponse(serializer.data)

@csrf_exempt
def valvula_list(request):
    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':
        valvula = Valvula.objects.all()
        serializer = ValvulaSerializer(valvula, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ValvulaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
        
@csrf_exempt
def opciones_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        opciones = Opciones.objects.get(pk=pk)
    except Opciones.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OpcionesSerializer(opciones)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OpcionesSerializer(opciones, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        opciones.delete()
        return HttpResponse(status=204)

@csrf_exempt
def opciones_list(request):
    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':
        opciones = Opciones.objects.all()
        serializer = OpcionesSerializer(opciones, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OpcionesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
 
# Jose

@csrf_exempt
def opciones_dispositivo_detail(request, pk):
    try:
        opciones = Opciones.objects.get(diapositivos_id=pk)
    except Opciones.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OpcionesSerializer(opciones)
        return JSONResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ValvulaSerializer(opciones, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def valvula_dispositivo_detail(request, pk):
    try:
        valvula = Valvula.objects.get(diapositivos_id=pk)
    except Valvula.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ValvulaSerializer(valvula)
        return JSONResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ValvulaSerializer(valvula, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def usuario_correo_detail(request, pk):
    try:
        usuario = Profile.objects.get(correo=pk)
    except Profile.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProfileSerializer(usuario)
        return JSONResponse(serializer.data)

@csrf_exempt
def dispositivo_usuario_detail(request, pk):
    try:
        dispositivo = Dispositivos.objects.get(usuarios_id=pk)
    except Dispositivos.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DispositivosSerializer(dispositivo)
        return JSONResponse(serializer.data)