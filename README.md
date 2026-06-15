# ♻️ Catálogo de Reciclagem

🌍 **Aplicação Online:** [Acesse o Catálogo Aqui](https://catalogo-reciclagem-gabriel-andrade.onrender.com)

**Versão:** 1.1.0

## 🎯 O Problema
Muitas pessoas desejam descartar materiais recicláveis ou perigosos (como pilhas, baterias, óleo de cozinha e lixo eletrônico) de forma correta, mas desconhecem os pontos de coleta próximos às suas residências. Isso gera acúmulo de lixo tóxico ou descarte irregular no meio ambiente.

## 💡 A Solução
O **Catálogo de Reciclagem** é uma aplicação web simples que permite listar e visualizar pontos de descarte reciclável. A aplicação visa conectar o cidadão aos locais adequados de coleta, promovendo a sustentabilidade e facilitando o acesso à informação. O sistema também conta com integração à API do ViaCEP para busca automática de localidade.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3
* **Framework:** Django 6.x
* **Integração:** API REST (ViaCEP)
* **Banco de Dados:** PostgreSQL (Hospedado no Supabase)
* **Qualidade de Código:** Flake8 (Linting) e GitHub Actions (CI/CD)
* **Hospedagem (Deploy):** Render e Gunicorn

## 🚀 Como instalar e executar

1. **Clone este repositório:**

    git clone <https://github.com/biel-acouto/catalogo_reciclagem.git>

2. Acesse a pasta do projeto:

    cd catalogo_reciclagem

3.Crie e ative o ambiente virtual:

    * Windows: python -m venv venv e depois venv\Scripts\activate
    * Linux/Mac: python3 -m venv venv e depois source venv/bin/activate

4. Instale as dependências:

        pip install -r requirements.txt

5. Configure as Variáveis de Ambiente:

    Crie um arquivo chamado .env na raiz do projeto (na mesma pasta do manage.py) e adicione as seguintes chaves de configuração:
    

        SECRET_KEY=sua_chave_secreta_django
        DATABASE_URL=postgresql://usuario:senha@host:porta/banco

6. Crie o banco de dados e rode o servidor:

        python manage.py migrate

        python manage.py runserver

    Acesse (http://127.0.0.1:8000/) no seu navegador.

## 🧪 Como rodar os testes

A aplicação possui testes automatizados. Para executá-los, utilize o comando: 

        python manage.py test

(Caso o banco de dados local esteja retendo a sessão, utilize python manage.py test --keepdb)

## 🧹 Como rodar o Linting

Para verificar a formatação e a qualidade estática do código, execute: 

        flake8


## 👨‍💻 Autor

Gabriel Andrade Couto