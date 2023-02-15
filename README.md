# Agenda-Web

Simples aplicação web para **Agenda de Eventos** usando Python Django, SQLite3 e HTML.

Projeto feito com referência ao curso Desenvolvimento para Internet e Banco de Dados com Python e Django, professor Rafael Galleani, Digital Innovation One - DIO

Siga as etapas abaixo para configurações, download e execução do projeto:

1. ### Ambiente
- Prepare o diretório para o código do projeto e ambiente virtual:
    ```
    mkdir agenda-web && cd agenda-web
    ```
- Crie um novo ambiente virtual:
    ```
    python3 -m venv agenda-venv
    ```
- Em seguida ative o ambiente virtual:
    ```
    source agenda-venv/bin/activate # No caso do Linux
    ./agenda-venv/Scripts/activate # No caso do Windows
    ```

2. ### Código Fonte
- Clone o código fonte do projeto:
    ```
    git clone https://github.com/rickeick/agenda-project.git
    ```
- Instale os requisitos no ambiente virtual:
    ```
    pip install -r agenda-project/requirements.txt
    ```

3. ### Banco de Dados
- Crie as tabelas do banco de dados:
    ```
    python3 agenda-project/manage.py migrate
    ```
- Crie uma nova conta de superusuário:
    ```
    python3 agenda-project/manage.py createsuperuser
    ```

4. ### Execução
- Execute o servidor de desenvolvimento:
    ```
    python3 agenda-project/manage.py runserver
    ```

- Em qualquer browser acesse: http://127.0.0.1:8000/admin e faça login.
