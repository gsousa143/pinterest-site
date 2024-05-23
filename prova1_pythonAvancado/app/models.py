from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Imagem(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.TextField(null = True)


    def __str__(self):
        return self.titulo


class Usuario(User):
    galeria = models.ManyToManyField(Imagem)


