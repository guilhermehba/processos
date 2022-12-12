from django.db import models

# Create your models here.
class Parametro (models.Model):
    nome = models.CharField(max_length=256, verbose_name='Nome do Parametro')
    valor = models.CharField(max_length=512, verbose_name='Valor do Parametro')

    class Meta:
        db_table = 'Parametros_Server'
    def __str__(self):
        return self.nome