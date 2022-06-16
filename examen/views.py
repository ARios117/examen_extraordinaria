from django.shortcuts import render
from django.views import generic
from .models import Bicicleta, Alquiler, Cliente

# Create your views here.

def lista_alquileres(request):

    context_dict = {}

    try:
        context_dict['alquileres'] = Alquiler.objects.filter(cliente__id=1001)
        context_dict['error'] = None

    except BaseException:

        context_dict['error'] = "Cliente no encontrado."
        context_dict['alquileres'] = None

    return render(request, 'examen/cliente_detail.html', context_dict)


class ClienteDetailView(generic.DetailView):
    model = Cliente


def show_cliente(request, slug):

    context_dict = {}

    try:
        cliente = Cliente.objects.get(slug=slug)

        context_dict['cliente'] = cliente
        context_dict['alquileres'] = Alquiler.objects.filter(cliente__id=cliente.id)

    except Cliente.DoesNotExist:

        context_dict['cliente'] = None
        context_dict['alquileres'] = None


    return render(request, 'examen/cliente_detail.html', context_dict)