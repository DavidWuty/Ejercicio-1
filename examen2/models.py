from django.db import models

# Create your models here.

class Mascota(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    especie = models.CharField(max_length=30,choices=[("Perro","Perro"),("Gato","Gato"),("Hamster","Hamster"),("Perico","Perico"),("Pez","Pez")])
    genero = models.CharField(max_length=30,choices=[("Macho","Macho"),("Hembra","Hembra")])
    creado = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"{self.nombre}---{self.creado}"
    