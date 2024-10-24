from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User





class FormularioDeCreacionDeUsuario(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)  # Corregido aquí

    # Permite contener información de configuración de formulario
    class Meta:
        model = User
        # Indico los campos que quiero que muestre
        fields = ['username', 'email', 'password1', 'password2']
        # Limpia los mensajes de textos
        help_texts = {key: '' for key in fields}