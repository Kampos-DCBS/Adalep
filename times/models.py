from django.db import models

class Time(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    fundacao = models.IntegerField()

    def __str__(self):
        return self.nome