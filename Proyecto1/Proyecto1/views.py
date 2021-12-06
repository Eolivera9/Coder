from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader

def saludo(request):
    return HttpResponse("Soy Ezequiel - Hola Django - Coder")

def segundaVista(request):
    return HttpResponse("<br><br> -----------------YA SOMOS PROGRAMADORES WEB")

def dia(request):

    variable = datetime.now()

    return HttpResponse(f"Hoy es un gran dia from <br>{variable}")

def apellido(request, ape):

    fecha = datetime.now()

    return HttpResponse(f"El profe coder {ape} es muy bueno <br><br> Por lo menos hoy {fecha}")

def cuantosAniosTengo(Request, nac):

    return HttpResponse (f"Mi edad es: {datetime.year(datetime.now())}")

def probandoTemplate(request):

    mejorEstudiante = "Ezequiel Cantarero"

    nota = 9.5

    fecha = datetime.now()

    estudiantesMasSimpaticos = ["Juanse", "Nadia", "Cristo"]

    dicc = {"nombre": mejorEstudiante, "nota": nota, "fechaActual": fecha, "estudiantes": estudiantesMasSimpaticos}

    plantilla = loader.get_template("template1.html")

    #miHtml = open("C:/Users/ezequ/PycharmProjects/ProyectoCoder/pruebaCoder1/Proyecto1/Proyecto1/Plantillas/template1.html")

    #plantilla = Template(miHtml.read())

    #miHtml.close()

    #miContexto = Context(dicc)

    #documento = plantilla.render(miContexto)

    documento = plantilla.render(dicc)

    return HttpResponse(documento)