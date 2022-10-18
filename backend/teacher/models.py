from django.db import models


class Professor(models.Model):
    nome = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Nome'
    )
    valor_hora = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        null=False,
        blank=False,
        verbose_name='Valor/Hora'
    )
    descricao = models.TextField(
        null=False,
        blank=False,
        verbose_name='Descrição'
    )
    foto = models.URLField(max_length=255, null=False, blank=False)


class Aula(models.Model):
    nome = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Nome'
    )
    email = models.EmailField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Email'
    )
    professor = models.ForeignKey(
        to=Professor,
        on_delete=models.CASCADE,
        related_name='aula_professor',
        verbose_name='Professor'
    )