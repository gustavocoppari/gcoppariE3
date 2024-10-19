from django import forms

class CrearPersonaFormulario(forms.Form):  
    dni = forms.CharField() #(max_length=9)
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    empresa = forms.CharField(max_length=20)
    
    
class BuscarPersonaFormulario(forms.Form):
        apellido = forms.CharField(max_length=20,required=False)
        empresa = forms.CharField(max_length=20,required=False)
        
        
        