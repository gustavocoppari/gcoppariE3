from django.http import HttpResponse
from django.template import Template, Context, loader

from django.shortcuts import render, redirect, get_object_or_404
from inicio.models import Persona
from inicio.forms import CrearPersonaFormulario,BuscarPersonaFormulario,EditarPersonaFormulario


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



def about(request):
    return render(request, 'inicio/about.html')


def verpersona(request,persona_id):
     # Buscamos la persona por su ID o devolvemos un 404 si no existe)
    persona=Persona.objects.get( id=persona_id)
     # Pasamos la persona al template
    return render(request, 'inicio/verpersona.html', {'p': persona})





def eliminarpersona(request,persona_id):
   
    persona=Persona.objects.get( id=persona_id)
    persona.delete()
    return redirect('inicio:buscar_persona')

          
            
           


def editarpersona(request, persona_id):
    # Obtener la persona con el ID proporcionado
    persona = Persona.objects.get(id=persona_id)
    
    # Inicializar el formulario con los datos actuales de la persona
    formulario = EditarPersonaFormulario(initial={
        'dni': persona.dni,
        'nombre': persona.nombre,
        'apellido': persona.apellido,
        'empresa': persona.empresa
    })
    
    # Si la solicitud es POST (se ha enviado el formulario)
    if request.method == 'POST':
        formulario = EditarPersonaFormulario(request.POST, instance=persona)
        
        # Si el formulario es válido, actualizamos los datos de la persona
        if formulario.is_valid():
            formulario.save()  # Guardamos los datos actualizados
            return redirect('inicio:buscar_persona')  # Redirigimos tras guardar
    
    # Renderizamos la plantilla con el formulario
    return render(request, 'inicio/editarpersona.html', {
        'persona': persona,
        'form': formulario
    })

