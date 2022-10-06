from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class persona(models.Model):
    nombre=models.CharField(max_length=25)
    apellido=models.CharField(max_length=25)
    edad=models.IntegerField()
    def __str__(self):
        return self.nombre
   



