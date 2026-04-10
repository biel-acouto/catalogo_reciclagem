# ♻️ Catálogo de Reciclagem

**Versão:** 1.0.3

## 🎯 O Problema
Muitas pessoas desejam descartar materiais recicláveis ou perigosos (como pilhas, baterias, óleo de cozinha e lixo eletrônico) de forma correta, mas desconhecem os pontos de coleta próximos às suas residências. Isso gera acúmulo de lixo tóxico ou descarte irregular no meio ambiente.

## 💡 A Solução
O **Catálogo de Reciclagem** é uma aplicação web simples que permite listar e visualizar pontos de descarte reciclável. A aplicação visa conectar o cidadão aos locais adequados de coleta, promovendo a sustentabilidade e facilitando o acesso à informação.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3
* **Framework:** Django
* **Banco de Dados:** SQLite (padrão do Django)
* **Qualidade de Código:** Flake8 (Linting) e GitHub Actions (CI)

## 🚀 Como instalar e executar

1. Clone este repositório:

    git clone <https://github.com/biel-acouto/catalogo_reciclagem.git>

2. Acesse a pasta do projeto:

    cd catalogo_reciclagem

3.Crie e ative o ambiente virtual:

    * Windows: python -m venv venv e depois venv\Scripts\activate
    * Linux/Mac: python3 -m venv venv e depois source venv/bin/activate

4. Instale as dependências:

    pip install -r requirements.txt

5. Crie o banco de dados e rode o servidor:

    python manage.py migrate
    python manage.py runserver
    Acesse http://127.0.0.1:8000/ no seu navegador.

## 🧪 Como rodar os testes

A aplicação possui testes automatizados. Para executá-los, utilize o comando: 
        python manage.py test

## 🧹 Como rodar o Linting

Para verificar a formatação e a qualidade estática do código, execute:  
        flake8


## 👨‍💻 Autor

Gabriel Andrade Couto