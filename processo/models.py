from django.db import models
from django.db.models.fields import DateTimeField
from django.core.validators import FileExtensionValidator
import json


STATUS_CHOICE = (
        (u"C", "Cadastrado"),
        (u"P", "Publicado")
    )

class Gerencia (models.Model):

    nome = models.CharField(
        verbose_name='Nome',
        max_length=150,
        help_text='Nome Completo'
        )
    class Meta:
        db_table = 'gerencia'
    def __str__(self):
        return self.nome


class Macro(models.Model):

    gerencia = models.ForeignKey('Gerencia', on_delete=models.PROTECT)
    nome = models.CharField(
        verbose_name='Nome do Macro',
        max_length=150,
        help_text='Nome do Macro'
        )
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, blank=False, null=False)

    class Meta:
        db_table = 'macro'
    def __str__(self):
        return self.nome


class Processo(models.Model):

    macro=models.ForeignKey('Macro',on_delete=models.PROTECT)
    nome = models.CharField(
        verbose_name='Nome do Processo',
        max_length=150,
        help_text='Nome do Processo'
        )
    descricao=models.TextField(blank=True, help_text='Descrição do Processo')
    data=models.DateField(auto_now_add=True)
    processo = models.FileField(upload_to='processo', )
    #validators=[FileExtensionValidator(allowed_extensions=['zip'])]
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, blank=False, null=False)
    class Meta:
        db_table = 'processo'

    def __str__(self):
        return self.nome

class search (models.Model):
    nome = models.ForeignKey ('processo.gerencia', on_delete=models.PROTECT)
    nome = models.ForeignKey ('processo.macro', on_delete=models.PROTECT)
    nome = models.ForeignKey ('processo.processo', on_delete=models.PROTECT)