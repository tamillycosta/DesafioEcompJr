# DesafioEcompJr

# Backend do Projeto To-do List

Este documento descreve a estrutura do backend, detalhando o banco de dados, endpoints, e o funcionamento do projeto.

## Sumário

- [Banco de Dados](#banco-de-dados)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Configuração](#configuração)


## Banco de Dados

O banco de dados do projeto foi projetado para gerenciar as informações de usuários e tarefas no sistema. A seguir, apresentamos o Diagrama UML, que ilustra a estrutura das tabelas e seus relacionamentos, bem como o Diagrama de Casos de Uso, que descreve as interações principais do sistema.

### Diagrama UML
O diagrama UML abaixo mostra a estrutura do banco de dados, com as tabelas e os relacionamentos entre usuários e tarefas:

![DiagramaUmlEcompJrs](https://github.com/user-attachments/assets/c21a6615-c5a1-44b9-8d82-f29e63be9d5f)

### Diagrama de Casos de Uso
Este diagrama de casos de uso detalha as funcionalidades principais do sistema, ilustrando as interações entre os usuários e o sistema em diferentes cenários:

![DiagramaCasosdeUsoEcompJrs](https://github.com/user-attachments/assets/f9525fa2-d433-4534-a68f-87b5a266e326)


## Estrutura do Projeto

1. Database (Banco de Dados)
A camada de Database gerencia a estrutura e persistência dos dados. Utiliza-se o SQLAlchemy como ORM (Object-Relational Mapping) para interagir com o banco de dados de forma abstrata. Nesta camada, estão definidas as tabelas e seus relacionamentos, representados como classes Python que mapeiam para as tabelas no banco de dados.

Estrutura das tabelas: Cada entidade (como User e Task) é representada por uma classe em Python, contendo atributos que correspondem às colunas das tabelas no banco de dados.


2. Repository (Repositório)
A camada de Repository gerencia a conexão direta com o banco de dados e implementa as operações de CRUD (Create, Read, Update, Delete). O repositório se comunica com o banco através do SQLAlchemy, encapsulando as operações de banco de dados, de modo que a camada de serviço não precise lidar diretamente com SQL.


4. Service (Serviço)
A camada de Service contém a lógica de negócios e realiza a comunicação com o repositório. Ela é responsável por processar as requisições e aplicar regras de negócio, antes de interagir com o repositório para realizar operações de leitura ou escrita no banco de dados.


4 Controller (Controlador)
A camada de Controller processa as requisições HTTP que chegam à aplicação e coordena a resposta correta através da comunicação com os serviços. É responsável por lidar com as entradas do usuário (via rotas HTTP) e garantir que as respostas apropriadas sejam devolvidas.


5. Routers (Rotas)
A camada de Routers define as rotas da aplicação, mapeando URLs para as funções do controlador. Cada rota está associada a uma função específica do controlador, que por sua vez comunica-se com os serviços e retorna a resposta adequada.
A documentação das rotas poder acessada em : http://localhost:8000/docs


 
 ## Configuração de Ambiente 

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
    ```
    python/python3 main.py
    Abra o navegador e acesse http://localhost:8000/.

    
