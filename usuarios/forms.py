from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import DatosExtra



class FormularioDeCreacionDeUsuario(UserCreationForm):
    # Campos existentes
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        help_texts = {key: '' for key in fields}




class FormularioEdicionPerfil(UserChangeForm):
    email = forms.EmailField(label='Correo electrónico')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    avatar = forms.ImageField(required=False)
    fecha_nacimiento = forms.DateField(required=False, label='Fecha de Nacimiento', widget=forms.DateInput(attrs={'type': 'date'}))
    lugar_nacimiento = forms.CharField(required=False, label='Lugar de Nacimiento')
    hobbies = forms.CharField(required=False, label='Hobbies', widget=forms.Textarea(attrs={'rows': 3}))
    direccion = forms.CharField(required=False, label='Dirección')
    password = None
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'avatar', 'fecha_nacimiento', 'lugar_nacimiento', 'hobbies', 'direccion']
