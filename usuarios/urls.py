from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings
from .views import editar_usuario,lista_usuarios,chat

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('perfil/editar-perfil', views.editar_perfil, name='editar_perfil'),
    path('perfil/cambiar_pass', views.cambiar_pass.as_view(), name='cambiar_pass'),
    path('editar-usuario/<int:usuario_id>/', editar_usuario, name='editar_usuario'),
    path('lista-usuarios/', lista_usuarios, name='lista_usuarios'),
    path('chat/', views.chat_view, name='chat'),
    path('delete_message/<int:message_id>/', views.delete_message, name='delete_message'),
    path('borrar/<int:usuario_id>/', views.borrar_usuario, name='borrar_usuario')

    
    # chat 
    #path('chat/', views.chat_view, name='chat'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)