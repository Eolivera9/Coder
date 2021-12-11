from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Estadio
from AppCoder.forms import EstadioFormulario
# Create your views here.

def inicio(request):

    return render(request, 'AppCoder/inicio.html')

def jugadores(request):

    return render(request, 'AppCoder/jugadores.html')

def estadioFormulario(request):

    if request == "POST":

        miFormulario = EstadioFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            estadio = Estadio(request.POST["direccion"], request.POST["anioFund"])

            estadio.save()

            return render(request, 'AppCoder/inicio.html')

    else:

        miFormulario = EstadioFormulario()

    return render(request, 'AppCoder/estadioFormulario.html',{"miFormulario":miFormulario})

def equipos(request):

    return render(request, 'AppCoder/equipos.html')
