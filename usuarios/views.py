from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm, UserChangeForm
from django.contrib import messages
from usuarios.forms import FormularioDeCreacionDeUsuario, FormularioEdicionPerfil
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import DatosExtra

from django.contrib.auth.models import User


from .models import Message







#Para el modelo de mensajeria
from django.contrib.auth.models import User
from .models import Mensaje




def login(request):
    # Si el método es GET, se muestra el formulario vacío
    if request.method == 'GET':
        formulario = AuthenticationForm()
    else:
        # Si el método es POST, procesamos los datos del formulario
        formulario = AuthenticationForm(data=request.POST)
        if formulario.is_valid():

            userr = formulario.get_user()
            if userr is not None:
                django_login(request, userr)  # Autenticamos al usuario
                DatosExtra.objects.get_or_create(user=userr)
                messages.success(request, f"Bienvenido {userr}")
                return redirect('inicio:inicio')  # Redirige a una página, por ejemplo, la de inicio
            else:
                messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, 'usuarios/login.html', {'form': formulario})






def register(request):
    if request.method == 'POST':
        form = FormularioDeCreacionDeUsuario (request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            if User.objects.filter(username=username).exists():
                messages.error(request, 'El nombre de usuario ya está en uso. Elige otro.')
            else:
                form.save()
                messages.success(request, 'Usuario registrado exitosamente.')
                return redirect('usuarios:login')
    else:
        form = FormularioDeCreacionDeUsuario ()
    return render(request, 'usuarios/register.html', {'form': form})




@login_required
def editar_perfil(request):
    datos_extra, created = DatosExtra.objects.get_or_create(user=request.user)
    formulario = FormularioEdicionPerfil(
        request.POST or None,
        request.FILES or None,
        instance=request.user,
        initial={
            'fecha_nacimiento': datos_extra.fecha_nacimiento,
            'lugar_nacimiento': datos_extra.lugar_nacimiento,
            'hobbies': datos_extra.hobbies,
            'direccion': datos_extra.direccion,
        }
    )

    if request.method == "POST" and formulario.is_valid():
        new_avatar = formulario.cleaned_data.get('avatar')
        if new_avatar:
            datos_extra.avatar = new_avatar

        datos_extra.fecha_nacimiento = formulario.cleaned_data.get('fecha_nacimiento')
        datos_extra.lugar_nacimiento = formulario.cleaned_data.get('lugar_nacimiento')
        datos_extra.hobbies = formulario.cleaned_data.get('hobbies')
        datos_extra.direccion = formulario.cleaned_data.get('direccion')

        datos_extra.save()
        formulario.save()

        messages.success(request, "Perfil actualizado correctamente.")
        return redirect('inicio:inicio')

    # Obtener la lista de usuarios para el chat, excluyendo al usuario actual
    usuarios_para_chat = User.objects.exclude(id=request.user.id)
    
    return render(request, 'usuarios/editar_perfil.html', {
        'form': formulario,
        'usuarios_para_chat': usuarios_para_chat  # Agrega los usuarios al contexto
    })





class cambiar_pass(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/cambiar_password.html' 
    success_url = reverse_lazy('usuarios:editar_perfil')
    
    








@user_passes_test(lambda u: u.is_superuser)
def editar_usuario(request, usuario_id):
    user = get_object_or_404(User, id=usuario_id)
    datos_extra, _ = DatosExtra.objects.get_or_create(user=user)
    
    formulario = FormularioEdicionPerfil(request.POST or None, request.FILES or None, instance=user, initial={
        'fecha_nacimiento': datos_extra.fecha_nacimiento,
        'lugar_nacimiento': datos_extra.lugar_nacimiento,
        'hobbies': datos_extra.hobbies,
        'direccion': datos_extra.direccion,
    })
    
    if request.method == "POST" and formulario.is_valid():
        new_avatar = formulario.cleaned_data.get('avatar')
        if new_avatar:
            datos_extra.avatar = new_avatar

        datos_extra.fecha_nacimiento = formulario.cleaned_data.get('fecha_nacimiento')
        datos_extra.lugar_nacimiento = formulario.cleaned_data.get('lugar_nacimiento')
        datos_extra.hobbies = formulario.cleaned_data.get('hobbies')
        datos_extra.direccion = formulario.cleaned_data.get('direccion')

        datos_extra.save()
        formulario.save()

        messages.success(request, f"Perfil de {user.username} actualizado correctamente.")
        return redirect('usuarios:lista_usuarios')

    return render(request, 'usuarios/editar_usuario.html', {'form': formulario, 'usuario': user})




@user_passes_test(lambda u: u.is_superuser)
def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})



@login_required
def chat(request):
    # Obtener la lista de usuarios excluyendo al usuario actual
    usuarios_para_chat = User.objects.exclude(id=request.user.id)
    return render(request, 'usuarios/chat.html', {'usuarios_para_chat': usuarios_para_chat})




@login_required
def chat_view(request):
    if request.method == "POST":
        content = request.POST.get('content')
        if content:
            Message.objects.create(user=request.user, content=content)
            return redirect('usuarios:chat')  # Redirige a la misma página para refrescar

    messages = Message.objects.all().order_by('timestamp')
    return render(request, 'usuarios/chat.html', {'messages': messages})





@login_required
@user_passes_test(lambda u: u.is_staff)  # Solo el personal autorizado (admin)
def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    message.delete()
    return redirect('usuarios:chat')






def borrar_usuario(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)
    usuario.delete()
    return redirect('usuarios:lista_usuarios')
