from django.urls import path
from inicio.views import inicio, buscar_persona, crear_persona, about


app_name ='inicio'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('buscar-persona/', buscar_persona, name='buscar_persona'),
    path('crear-persona/', crear_persona, name='crear_persona'),
    path('about/', about, name='about')
]