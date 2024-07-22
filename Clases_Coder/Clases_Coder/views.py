from datetime import datetime as dt

from django.template import Template, Context
from django.http import HttpResponse

from django.template import loader

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
    nombre = "Gaston"
    apellido = "Holovaty"
    diccionario = {
        "nombre": nombre,
        "apellido": apellido,
        "notas": [4, 8, 9,10, 7, 8]
        
    }
    plantilla = loader.get_template('index.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)