from django.db import models

class Persona(models.Model):
    dni = models.IntegerField()
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    empresa = models.CharField(max_length=20)
    

    def __str__(self):
        # para mostra la lista datos
        return f'{self.nombre }{' '}{ self.apellido }{' - '}{ self.empresa }'
    
    
