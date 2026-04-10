from django.test import TestCase
from django.urls import reverse
from .models import PontoDeColeta


class PontoDeColetaTestCase(TestCase):

    def setUp(self):
        # Esse método roda antes de cada teste para preparar os dados
        self.ponto = PontoDeColeta.objects.create(
            nome="EcoPonto Teste",
            endereco="Rua Fictícia, 99",
            materiais_aceitos="Papelão, Plástico"
        )

    # Teste 1: Valida se o ponto foi criado corretamente (Caminho Feliz)
    def test_ponto_criado_com_sucesso(self):
        ponto_banco = PontoDeColeta.objects.get(nome="EcoPonto Teste")
        self.assertEqual(ponto_banco.endereco, "Rua Fictícia, 99")

    # Teste 2: Valida o retorno do método __str__ do modelo
    def test_str_do_modelo(self):
        self.assertEqual(str(self.ponto), "EcoPonto Teste")

    # Teste 3: Valida se a página inicial carrega e exibe o ponto criado
    def test_pagina_inicial_carrega_corretamente(self):
        resposta = self.client.get(reverse('home'))
        self.assertEqual(resposta.status_code, 200)  # 200 significa "OK" na web
        self.assertContains(resposta, "EcoPonto Teste")
