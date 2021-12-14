from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Estadio, Equipo
from AppCoder.forms import EstadioFormulario
# Create your views here.

def inicio(request):

    return render(request, 'AppCoder/inicio.html')

def jugadores(request):

    return render(request, 'AppCoder/jugadores.html')

def estadioFormulario(request):

    if request.method == "POST":

        miFormulario = EstadioFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            estadio = Estadio(direccion=informacion["direccion"] ,anioFund= informacion["anioFund"])

            estadio.save()

            return render(request, 'AppCoder/inicio.html')

    else:

        miFormulario = EstadioFormulario()

    return render(request, 'AppCoder/estadioFormulario.html',{"miFormulario":miFormulario})

def equipos(request):

    return render(request, 'AppCoder/equipos.html')

def busquedaEquipo(request):

    return render(request, 'AppCoder/busquedaEquipo.html')

def buscar(request):

    if request.GET["nombre"]:

        nombre = request.GET["nombre"]

        equipos = Equipo.objects.filter(nombre_icontains=nombre)

        #respuesta = f"Estoy buscando a: {request.GET['nombre']}"

        return render(request, "AppCoder/resultadoBusqueda.html", {"nombre":nombre, "ciudad":ciudad })



    else:
        respuesta = "Che, mandame informacion"

    return HttpResponse(respuesta)
