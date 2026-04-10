from django.db import models


class PontoDeColeta(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome do Local")
    endereco = models.CharField(max_length=255, verbose_name="Endereço Completo")
    materiais_aceitos = models.TextField(
        verbose_name="Materiais Aceitos",
        help_text="Ex: Pilhas, Baterias, Óleo de Cozinha, Eletrônicos"
    )

    def __str__(self):
        return self.nome
