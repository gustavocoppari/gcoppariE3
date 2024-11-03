from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView
from eventos.models import Fiesta
from django.urls import reverse_lazy
from django.db.models import Q



#def crear_fiesta(request):
#    return HttpResponse('Crear Fiesta')


class CrearFiesta(CreateView):
    model = Fiesta
    template_name = "eventos/crear_fiesta.html"
    success_url = reverse_lazy('eventos:listado_fiesta')
    fields = ['salon', 'direccion', 'construido', 'capacidad', 'imagen']  # Incluye el campo de imagen
    

class ListadoFiesta(ListView):
    model = Fiesta
    template_name = "eventos/lista_fiesta.html"
    context_object_name = 'fiestas'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(
                Q(salon__icontains=query) | 
                Q(direccion__icontains=query)
            )
        return queryset

class VerFiesta(DetailView):
    model= Fiesta
    template_name = "Eventos/ver_fiesta.html"
    
    
class EditarFiesta(UpdateView):
    model= Fiesta
    template_name = "Eventos/editar_fiesta.html"
    success_url = reverse_lazy('eventos:listado_fiesta')
    fields = ['salon', 'direccion', 'construido', 'capacidad', 'imagen']  # Incluye el campo de imagen

    
    
class EliminarFiesta(DeleteView):
    model= Fiesta
    template_name = "Eventos/eliminar_fiesta.html"
    success_url = reverse_lazy('eventos:listado_fiesta')
   # fields = ['salon', 'direccion','construido','capacidad']
   
   

