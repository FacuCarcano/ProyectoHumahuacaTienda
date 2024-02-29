from django.shortcuts import render, HttpResponse
from ServiciosApp.models import Servicio, CategoriaCatalogo
# Create your views here.

def servicios(request):
    variable_servicios = Servicio.objects.all
    return render(request, "servicios/servicios.html", {"variable_servicios" : variable_servicios})

def categoria(request, categoria_id):
   categoria = CategoriaCatalogo.objects.get(id=categoria_id)
   variable_servicios = Servicio.objects.filter(categorias=categoria)
   return render(request,"servicios/categorias.html", {"categoria":categoria, "variable_servicios" : variable_servicios})