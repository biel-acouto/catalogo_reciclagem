from django.shortcuts import render
from .models import PontoDeColeta
import requests


def home(request):
    pontos = PontoDeColeta.objects.all()
    endereco_busca = None
    erro = None

    # Verifica se o usuário digitou um CEP na URL (via GET)
    cep = request.GET.get('cep')

    if cep:
        # Limpa o CEP deixando apenas os números
        cep = ''.join(filter(str.isdigit, cep))

        if len(cep) == 8:
            # Faz a requisição HTTP GET para a API pública do ViaCEP
            resposta = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

            if resposta.status_code == 200:
                dados = resposta.json()
                if 'erro' not in dados:
                    # Separamos em variáveis para respeitar o limite de caracteres do Flake8
                    logradouro = dados['logradouro']
                    bairro = dados['bairro']
                    cidade = dados['localidade']
                    uf = dados['uf']

                    # Montamos a string final com o hífen e os espaços corretos
                    endereco_busca = f"{logradouro}, {bairro} - {cidade}/{uf}"
                else:
                    erro = "CEP não encontrado."
            else:
                erro = "Erro ao buscar o CEP na API."
        else:
            erro = "CEP inválido. Digite 8 números."

    return render(request, 'index.html', {
        'pontos': pontos,
        'endereco_busca': endereco_busca,
        'erro': erro
    })
