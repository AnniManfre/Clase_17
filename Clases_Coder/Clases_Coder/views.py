from datetime import datetime as dt

from django.template import Template, Context
from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola Anni, como estaas?")

def alejandro(request):
    texto = "Soy Alejandro que tal<br>Cursando Python."
    return HttpResponse(texto)

def dia_de_hoy(request, dia_personalizado):
    dia = dt.now()
    dia = dia.strftime("%Y-%m-%d")
    dia = dia[:-2] + dia_personalizado
    texto = f"Hoy es:<br>{dia}"
    return HttpResponse(texto)


def probando_template(request):

    #Abrimos el archivo html
    mi_html = open('./Clases_Coder/plantillas/index.html')
    
    #Creamos el template haciendo uso de la clase Template
    plantilla = Template(mi_html.read())
    
    #Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
    mi_html.close()
    
    #Creamos un contexto, mas adelante vamos a aprender a usarlo, ahora lo necesitamos aunque sea vacio
    mi_contexto = Context()
    
    #Terminamos de construir el template renderizandolo con su contexto
    documento = plantilla.render(mi_contexto)
    
    return HttpResponse(documento)