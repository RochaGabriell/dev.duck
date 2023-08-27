<h1 style='text-align: center'><a href="#">DEV.DUCK</a></h1>

<p style='text-align: justify;'>Trata-se do desenvolvimento de um sistema web, Dev.Duck, que tem como objetivo criar uma plataforma aberta e simples para que estudantes do curso de ADS possam publicar seus conhecimentos e experiências relacionados às matérias de suas grades curriculares.</p>
<p style='text-align: justify;'>Essa plataforma permite que os acadêmicos compartilhem links de matérias  complementares ou até texto de suas anotações das aulas, que poderão ser vistos na plataforma. Com o Dev.Duck, queremos oferecer aos estudantes uma maneira fácil de se conectar e aprender uns com os outros.</p>

---

<p align="center">
  <a href="#-Começando">Começando</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-Pré-requisitos">Pré-requisitos</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-Instalação">Instalação</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-Carregando Dados do Banco">Carregando Dados do Banco</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-Construído com">Construído com</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-Licença">Licença</a>
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.9%20%7C%203.10-blue" alt="Python"></a>
  <a href="https://www.djangoproject.com/"><img src="https://img.shields.io/badge/Django-4.2-brightgreen" alt="Django"></a>
  <a href="https://www.w3.org/TR/html52/"><img src="https://img.shields.io/badge/HTML-5-orange" alt="HTML"></a>
  <a href="https://www.w3.org/Style/CSS/"><img src="https://img.shields.io/badge/CSS-3-blueviolet" alt="CSS"></a>
  <img alt="License" src="https://img.shields.io/static/v1?label=license&message=MIT&color=49AA26&labelColor=000000">
</p>

<img alt="Home Page" src="https://github.com/RochaGabriell/ProjetoIntegradorI/blob/main/.github/Pages/Home.png?raw=true">

<details>
  <summary>Outras Telas</summary>
  <img alt="See Post" src="https://github.com/RochaGabriell/ProjetoIntegradorI/blob/main/.github/Pages/See_Post.png?raw=true">
  <img alt="Profile" src="https://github.com/RochaGabriell/ProjetoIntegradorI/blob/main/.github/Pages/Profile.png?raw=true">
  <img alt="New Post" src="https://github.com/RochaGabriell/ProjetoIntegradorI/blob/main/.github/Pages/New_Post.png?raw=true">
</details>

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

## 📋 Pré-requisitos

Você precisa ter duas principais dependências instaladas:

```
Python 3.10.6
Django 4.2.1
```

## 🔧 Instalação

### 1 - Passo: Clone

Realize um clone do projeto em seu computador

```
https://github.com/RochaGabriell/ProjetoIntegradorI.git
```

### 2 - Passo: Criação e Ativação do Ambiente Virtual

Crie um ambiente virtual na pasta raiz do projeto. No seu terminal use:

> Linux:

2.1 - Criação

```
python3 -m venv venv
```

2.2 - Ativação

```
source venv/bin/activate
```

> Para Windows ou Mac:

Consulte a documentação da linguagem [Python](https://docs.python.org/pt-br/3/library/venv.html)

### 3 - Passo: Instalação de depedências

É preciso instalar as depedências do projeto para o funcionamento correto. Com o seu ambiente virtual ativo use o comando no seu terminal:

```
pip install -r requirements.txt
```

### 4 - Configure os dados do arquivo [`.env`](https://django-environ.readthedocs.io/en/latest/)

Para a correta execução do projeto é necessário a configuração das variáveis de ambiente.

- Crie um arquivo `.env` na raiz do projeto

```
DJANGO_SECRET_KEY='Sua SECRET_KEY'

DATABASE_URL='URL que aponta para o banco de dados utilizado.'

EMAIL_HOST_USER='usuário para autenticação em um servidor de e-mail.'
EMAIL_HOST_PASSWORD='senha para autenticação em um servidor de e-mail.'
DEFAULT_FROM_EMAIL='endereço de e-mail padrão utilizado.'
```

### 5 - Passo: Realize as migrações

Isso garante que o seu banco de dados esteja sincronizado com a estrutura do seu projeto.

```
python manage.py migrate
```

### 6 - Passo: Executar o projeto

```
python manage.py runserver
```

```
http://localhost:8000/
```

Observações:

- Para derrubar todos os serviços, basta utilizar as teclas `CTRL+C`, que é o padrão dos terminais para matar processos.

## Carregando Dados do Banco

Para iniciar com dados iniciais ou de backup em nosso banco de dados, você pode usar o comando a seguir:

```bash
./manage.py loaddata db_backups/db.json
```

## 🔍 Funcionalidades

As principais funcionalidades da aplicação são:

- RF.01 - Login e Cadastro de usuários;
- RF.02 - Tela inicial;
- RF.03 - Criar uma postagem;
- RF.04 - Visualização de postagens;
- RF.05 - Edição de postagens;
- RF.06 - Avaliação de postagens;
- RF.07 - Editar perfil;
- RF.08 - Recuperação de senha;
- RF.09 - Área de administração;
- RF.10 - Filtro de conteúdo;
- RF.11 - Visualizar de perfil.

## 🛠️ Construído com

- [Python](https://www.python.org/) - Linguagem de programação amplamente usada em aplicações da Web.
- [JavaScript](https://www.javascript.com/) - Linguagem de programação usada para fazer páginas interativas da Internet.
- [Django Framework](https://www.djangoproject.com/) - O framework web usado na criação do projeto.
- [Showdown](https://showdownjs.com/) - Um conversor bidirecional Markdown para HTML escrito em Javascript!.
- [PostgreSQL](https://www.postgresql.org/) - Banco de dados utilizado ao fazer deploy.
- [HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML) - Estruturação da página
- [CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS) - Estilização da página

## 📄 Licença

#### Este projeto está sob a licença (MIT License) - veja o arquivo [LICENSE.md](https://github.com/RochaGabriell/ProjetoIntegradorI/blob/main/LICENSE) para detalhes.

---
