from django.shortcuts import render, HttpResponse
from .models import Producto, CategoriaProducto
# Create your views here.

def tienda(request):
    variable_productos = Producto.objects.all()
    return render(request, "tienda/tienda.html", {'variable_productos':variable_productos})

