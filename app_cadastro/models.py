from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=150, unique=True)
    senha = models.CharField(max_length=255) 

    def __str__(self):
        return self.nome