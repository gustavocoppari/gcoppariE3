from django import forms
from .models import Persona

class AutoFormularioBase(forms.Form):
    dni = forms.CharField() #(max_length=9)
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    empresa = forms.CharField(max_length=20)  

class CrearPersonaFormulario(AutoFormularioBase):...  
    
class EditarPersonaFormulario(forms.ModelForm):
    class Meta:
        model = Persona  # Vinculamos el formulario al modelo Persona
        fields = ['dni', 'nombre', 'apellido', 'empresa']  # Campos a mostrar en el formulario
      
class BuscarPersonaFormulario(forms.Form):
        apellido = forms.CharField(max_length=20,required=False)
        empresa = forms.CharField(max_length=20,required=False)
        
