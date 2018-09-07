from django.db import models


class Alert(models.Model):
    tipo = models.CharField(max_length = 20)
    cor = models.CharField(max_length = 20)
    modelo = models.CharField(max_length = 20)
    placa = models.CharField(max_length = 7)
    local = models.CharField(max_length = 255)
    descrição = models.CharField(max_length = 255)
    foto = models.FileField(upload_to='static', null=True, blank=True)
