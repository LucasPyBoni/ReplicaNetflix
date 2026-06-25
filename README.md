# Replica Netflix

Este projeto foi baseado na Netflix, contendo um catálogo de filmes organizado em categorias e uma interface inspirada na plataforma original. Os usuários podem navegar pelos conteúdos disponíveis e visualizar informações dos filmes cadastrados.

## Link do site
[Replica da Netflix](https://replicanetflix.onrender.com/)

## Principais Bibliotecas

Django, Pillow e as bibliotecas nativas do projeto.

## Explicação da linha de raciocínio

Primeiramente foi criado um projeto Django chamado **Hashflix**, responsável pelas configurações gerais do sistema, URLs principais e inicialização da aplicação.

### models.py

Responsável pela estrutura do banco de dados. Nele são definidos os modelos que representam os filmes cadastrados na plataforma, contendo informações como título, descrição, miniaturas e demais características necessárias para exibição no catálogo.

### views.py

Contém a lógica das páginas do sistema. É responsável por buscar os dados dos filmes armazenados no banco de dados e enviá-los para os templates, permitindo que sejam exibidos dinamicamente ao usuário.

### urls.py

Define as rotas da aplicação. Cada rota direciona o usuário para uma página específica do sistema, conectando as URLs às respectivas views.

### admin.py

Permite o gerenciamento dos filmes através do painel administrativo do Django, facilitando o cadastro, edição e remoção de conteúdos da plataforma.

### forms.py

Responsável pelos formulários utilizados na aplicação, permitindo a entrada e validação de dados enviados pelos usuários.

### templates

Contém os arquivos HTML responsáveis pela interface visual do sistema. As páginas foram adaptadas para serem dinâmicas, recebendo informações diretamente do banco de dados através do Django Template Language.

### media

Diretório utilizado para armazenar arquivos enviados para a aplicação, como imagens e miniaturas dos filmes.

### static

Armazena arquivos estáticos do projeto, como folhas de estilo (CSS), imagens e scripts JavaScript utilizados na interface.

## Funcionalidades

* Exibição de catálogo de filmes.
* Organização visual semelhante à Netflix.
* Cadastro e gerenciamento de filmes pelo painel administrativo.
* Upload e armazenamento de imagens dos filmes.
* Renderização dinâmica das informações utilizando Django.
* Interface responsiva baseada em templates HTML.

---

Ficaria com cara de documentação de portfólio/projeto acadêmico, semelhante ao README do Pinterest que você mostrou, mas adaptado para Django.
