# DesafioEcompJr

## Introdução

Este é um projeto de uma aplicação para gerenciar uma lista de tarefas. A proposta é criar uma interface amigável onde os usuários podem adicionar, editar e remover tarefas de forma intuitiva, melhorando a produtividade e a organização pessoal.



## Desenvolvedores

Este projeto foi desenvolvido por uma equipe colaborativa, onde cada membro trouxe suas habilidades e conhecimentos para a construção da aplicação. Abaixo estão os desenvolvedores e suas respectivas funções:

- **Tamilly Costa**: 
  - **Função**: Desenvolvedor Backend
  - **Responsabilidades**: Implementação da API com FastAPI, gerenciamento do banco de dados com SQLAlchemy, e lógica de negócios e integração com o Frontend.

- **Felipe Amorim**: 
  - **Função**: Desenvolvedor Frontend
  - **Responsabilidades**: Criação da interface do usuário com ReactJS, gerenciamento de estados e oganização geral  do projeto .
    

### Objetivos do Projeto

- **Gerenciamento de Tarefas:** Permitir que os usuários criem e mantenham uma lista de tarefas, facilitando o acompanhamento das atividades diárias.
- **Perfil de Adm:** Permitir que administradores possam gerenciar outros usuários  e tarefas.

### Tecnologias Utilizadas

- **FastAPI:** Um framework moderno e rápido para construir APIs com Python, que permite a criação de aplicações web de forma simples e eficiente.
- **SQLite:** Um banco de dados leve e autônomo que é fácil de configurar e perfeito para aplicações que não exigem um servidor de banco de dados complexo.
- **ReactJS:** Uma biblioteca JavaScript para construir interfaces de usuário, proporcionando uma experiência dinâmica e responsiva.

## Requisitos

- Node.js (versão 14 ou superior)
- npm (gerenciador de pacotes do Node)
- Python 3.7 ou superior
- pip (gerenciador de pacotes do Python)


## Configuração do Ambiente de Desenvolvimento


### Frontend 

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/tamillycosta/DesafioEcompJr.git
   cd DesafioEcompJr
   cd my-app


2. **Instale as dependências:**

     ```
      npm install


**Como Executar o Projeto**

1. **Execute o servidor **:

    `` npm start , Abra o navegador e acesse http://localhost:3000



### Backend 

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/tamillycosta/DesafioEcompJr.git
   cd DesafioEcompJr

2. **Crie ambiente virtual:**

    ``` No linux
        python3 -m venv venv
        source venv/bin/activate
    
    ``` No windows
        python -m venv venv
        venv\Scripts\activate


3. **Instale as dependências:**

     ```
      pip install -r requirements.txt


**Como Executar o Projeto**

1. **Execute o servidor FastAPI**:

    `` python/python3 main.py


   

## Estrutura do Projeto

A estrutura do projeto é organizada em camadas, seguindo o padrão de arquitetura em camadas para facilitar a manutenção e a escalabilidade.

### Backend

O backend da aplicação é responsável por gerenciar a lógica de negócios e a interação com o banco de dados. Ele utiliza **FastAPI** para criar uma API RESTful e **SQLAlchemy** para gerenciar a estrutura das tabelas no banco de dados **SQLite**. O backend é organizado da seguinte maneira:

- **Database:** Estrutura das tabelas usando SQLAlchemy.
- **Repository:** Gerencia a conexão com o banco de dados e implementa as operações de CRUD.
- **Service:** Realiza a comunicação com o repositório e contém a lógica de negócios.
- **Controller:** Processa as requisições HTTP e se comunica com os serviços.
- **Routers:** Define as rotas da aplicação, mapeando URLs às funções do controlador.

Para mais detalhes sobre a estrutura do backend, consulte o [README do Backend](https://github.com/tamillycosta/DesafioEcompJr/blob/Backend/README.md).



### Frontend

O frontend da aplicação é responsável pela interface do usuário e pela interação com o backend. Ele utiliza ReactJS para construir uma aplicação de página única (SPA) e se comunica com a API do backend. O frontend é organizado da seguinte maneira:

- **API**: Contém as requisições para o backend, gerenciando a comunicação com a API.
- **Pages**: Armazena as páginas da aplicação, incluindo os arquivos JavaScript e CSS correspondentes a cada página.
- **Components:** Componentes reutilizáveis que podem ser utilizados em várias páginas, como botões e formulários.

Para mais detalhes sobre a estrutura do frontend, consulte o [README do Frontend](https://github.com/tamillycosta/DesafioEcompJr/edit/frontend-dev/README.md).


