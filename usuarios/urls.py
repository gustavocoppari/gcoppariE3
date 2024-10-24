from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'  # Esto define el espacio de nombres

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout')
    
]