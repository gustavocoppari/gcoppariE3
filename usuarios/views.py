from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib import messages
from usuarios.forms import FormularioDeCreacionDeUsuario




def login(request):
    # Si el método es GET, se muestra el formulario vacío
    if request.method == 'GET':
        formulario = AuthenticationForm()
    else:
        # Si el método es POST, procesamos los datos del formulario
        formulario = AuthenticationForm(data=request.POST)
        if formulario.is_valid():

            user = formulario.get_user()
            if user is not None:
                django_login(request, user)  # Autenticamos al usuario
                messages.success(request, f"Bienvenido {user}")
                return redirect('inicio:inicio')  # Redirige a una página, por ejemplo, la de inicio
            else:
                messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, 'usuarios/login.html', {'form': formulario})





def register(request):
    form = FormularioDeCreacionDeUsuario()
    if request.method == 'POST':
        form = FormularioDeCreacionDeUsuario(request.POST)
        if form.is_valid():
            form.save()
          #  messages.success(request, 'Usuario creado exitosamente. ¡Ahora puedes iniciar sesión!')
            return redirect('usuarios:login')
    
    return render(request, 'usuarios/register.html', {'form': form})
