from django.shortcuts import render
from .forms import Formulario
# Create your views here.

def contacto(request):
    variable_formulario = Formulario()
    return render(request, "contacto/contacto.html", {'variable_formulario':variable_formulario})
