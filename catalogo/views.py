from django.shortcuts import render
from .models import PontoDeColeta


def home(request):
    # Pega todos os pontos de coleta cadastrados no banco
    pontos = PontoDeColeta.objects.all()
    # Envia esses dados para um arquivo HTML que vamos criar
    return render(request, 'index.html', {'pontos': pontos})
