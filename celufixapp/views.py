from django.shortcuts import render, get_object_or_404
from .models import Marcas, Telefonos, Repuestos
from django.shortcuts import redirect
# Create your views here.


def index(request):
    marcas = Marcas.objects.all()
    return render(request, 'index.html', {'marcas': marcas})


def telefonos(request, marca_id):
    marca = get_object_or_404(Marcas, id=marca_id)
    telefonos = Telefonos.objects.filter(marca=marca)
    return render(request, 'telefonos.html', {'telefonos': telefonos, 'marca': marca})




def repuestos(request, telefono_id):
    telefono = get_object_or_404(Telefonos, id=telefono_id)
    repuestos = Repuestos.objects.filter(telefono=telefono)
    return render(request, 'repuestos.html', {'repuestos': repuestos, 'telefono': telefono})


