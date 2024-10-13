from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render, redirect
from inicio.models import Persona
from inicio.forms import CrearPersonaFormulario,BuscarPersonaFormulario


def inicio(request):
    return render(request, 'inicio/index.html')



def buscar_persona(request):
    persona = None  # Inicializamos persona como None por defecto
    formulario = BuscarPersonaFormulario(request.GET)

    if formulario.is_valid():
        apellido = formulario.cleaned_data.get('apellido')
        empresa = formulario.cleaned_data.get('empresa')

        # Realizar la búsqueda solo si se han proporcionado datos
        persona = Persona.objects.filter(apellido__icontains=apellido, empresa__icontains=empresa)

    return render(request, 'inicio/buscar_persona.html', {
        'form': formulario,
        'persona': persona,  # Pasamos la variable persona al template
    })



# def buscar_persona(request):
    
#     formulario=BuscarPersonaFormulario(request.GET)
#     if formulario.is_valid():
#         apellido=formulario.cleaned_data.get('apellido')
#         empresa=formulario.cleaned_data.get('empresa')
#         persona=Persona.objects.filter(apellido__icontains=apellido,empresa__icontains=empresa)
          
#     return render(request,'inicio/buscar_persona.html',{'apellido': apellido,'form':formulario})




def crear_persona(request):
    
    formulario = CrearPersonaFormulario(request.POST)
    if request.method == 'POST':
       
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            # Crear y guardar el objeto 
            persona = Persona(dni=data.get('dni'), nombre=data.get('nombre'), apellido=data.get('apellido'), empresa=data.get('empresa'))
            persona.save()
            return redirect('inicio:buscar_persona')

        else:
            # En caso de que falten datos
            return render(request, 'inicio/crear_persona.html', {'error': 'Por favor completa todos los campos'})

    return render(request, 'inicio/crear_persona.html',{'form': formulario})
