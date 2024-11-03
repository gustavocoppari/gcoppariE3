from django.db import models

#GEnero
class Fiesta(models.Model):
    salon=models.CharField(max_length=20)
    direccion=models.CharField(max_length=20)
    construido=models.DateTimeField()
    capacidad=models.IntegerField()
    imagen = models.ImageField(upload_to='imagenes_fiestas/', blank=True, null=True)
    
    
    def __str__(self):
        return f'{self.salon} - {self.direccion} - capacida: {self.capacidad}'