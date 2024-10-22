from django.urls import path
from eventos import views

app_name='eventos'

urlpatterns = [
    path('fiestas/crear/', views.CrearFiesta.as_view(), name='crear_fiesta'),
    path('fiestas/', views.ListadoFiesta.as_view(), name='listado_fiesta'),
    path('fiestas/<int:pk>', views.VerFiesta.as_view(), name='ver_fiesta'),
    path('fiestas/<int:pk>/editar', views.EditarFiesta.as_view(), name='editar_fiesta'),
    path('fiestas/<int:pk>/eliminar', views.EliminarFiesta.as_view(), name='eliminar_fiesta')
]
