## Descrição

Crie um repositório publico utilizando GIT, e utilizando Python use a biblioteca Prefect (https://docs.prefect.io/latest/) para criar um projeto que consuma uma API externa (de sua preferencia) construindo tarefas (flow tasks) que consuma dados de pelo menos 2 endpoints relacionados, simulando timeout em um deles e utilizando retry, continuar o fluxo.
Armazene os dados obtidos em banco de dados com versionamento e exponha esses mesmos dados em formado CRUD utilizando RestAPI.

## Prefect

É uma framework de código aberto para criar fluxos de trabalho em python. Neste projeto foi simulado um timeout apenas na primeira tentativa de execução da task get_all_character_data. Como a task foi programada para fazer até 3 tentativas, ele dará sucesso nas próximas e continuará o fluxo chamando a segunda task

## Banco de dados

O banco de dados usado nesse projeto foi o PostgreSQL. Ele será criado ao executar o arquivo docker-compose

## Api Rest

Para construção da API foi utilizado o FastAPI que facilitou na criação dos endpoints

## Passo a passo de execução do projeto

Todos os comandos a seguir devem ser rodados na raiz do projeto:

1. Crie um ambiente virutal

```sh
python3.8 -m venv venv
```

2. Ative o ambiente virtual

```sh
source venv/bin/activate
```

3. Instale as dependências

```sh
pip install -r requirements.txt
```

4. Crie um banco de dados postgre

```sh
docker-compose up
```

5. Execute a main e verifique o timeout e a retentativa de retornar os dados da api

```sh
python main.py
```

6. Execute a API e teste os endpoints

```sh
uvicorn api.api:app --host 0.0.0.0 --port 8000 --reload
```

Para acessar a doc dos endpoints acesse:

- http://localhost:8000/docs
