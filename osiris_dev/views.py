from django.http import HttpResponse
import datetime
from django.template import Template, Context
# from django.template import loader
from django.template.loader import get_template
from django.shortcuts import render
from django.template import Context, Template, loader
from django.shortcuts import render
import datetime

def bienvenida(request):
    return HttpResponse("# bienvenido a OSIRIS")

def modulos(request):
    return HttpResponse("<p  style = 'color: red;' > Aca deben ir los modulos de los servicios a brindar <p>")

def categoria_edad (request, edad):
    if edad <= 18:
        categoria = 'menor de edad'
    if edad >= 18:
        categoria = 'mayor de edad'
    resultado = "<h1> categoria de la edad : %s<h1>" %categoria

    return HttpResponse(resultado)

def contenitdoHTML(request, nombre, edad):
    contenido = """
    
    """

def plantilla1(request):
    print("entro a la plantilla")
    plantillaExterna = open("C:\osiris_dev\osiris_dev\plantillas\plantilla_1.html") # cargo el html
    template = Template(plantillaExterna.read()) # abro el archivo y lo leo
    plantillaExterna.close() # cierro el archivo
    contexto = Context() # crear un contexto
    documento = template.render(contexto) # renderizar el documento
    return HttpResponse(documento)

def plantilla_parametros(request):
    nombre = 'Osiris'
    fecha = datetime.datetime.now()
    lenguajes = ['python', 'java', 'C++']
    print("entro a la plantilla")
    plantillaExterna = open("C:\osiris_dev\osiris_dev\plantillas\plantilla_parametros.html") # cargo el html
    template = Template(plantillaExterna.read()) # abro el archivo y lo leo
    plantillaExterna.close() # cierro el archivo
    contexto = Context({'nombre_canal':nombre, 'fecha': fecha, 'lenguajes': lenguajes}) # crear un contexto
    documento = template.render(contexto) # renderizar el documento
    return HttpResponse(documento)

def plantilla_cargador(request):
    nombre = 'Osiris'
    fecha = datetime.datetime.now()
    lenguajes = ['python', 'java', 'C++', 'Kotlin']
    # no olvidar la ruta donde estan las plantillas 
    plantillaExterna = loader.get_template('plantilla_parametros.html')
    #renderizamos el documento
    documento  = plantillaExterna.render({'nombre': nombre, 'fecha': fecha, 'lenguajes': lenguajes})
    return HttpResponse(documento)

def plantilla_shortcut(request):
    nombre = 'Osiris'
    fecha = datetime.datetime.now()
    lenguajes = ['python', 'java', 'C++', 'Kotlin', 'PROBANDO SHORTCUTS']
    # LEER DOCUMENTACION DE DJANGO CON RENDER 
    return render(request, 'plantilla_parametros.html', {'nombre': nombre, 'fecha': fecha, 'lenguajes': lenguajes} )

def plantillahija(request):
    return render(request, "plantillahija.html", {})

def plantillahija2(request):
    return render(request, "plantillahija2.html", {})



