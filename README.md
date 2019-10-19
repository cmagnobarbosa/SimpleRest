## Simple REST API in Python

Exemplo de servidor API rest simples em python utilizando flask.

## Endpoints

- /users - retorna um dicionário.

## Estrutura

```
  SimpleRest/
  |-- main.py
  |--simple_flask/
  |  |--endpoints/
        |--users.py
     | --models/
        |--db.py

```

## Dependências

- python3
- pip
    - >sudo apt-get install python3-pip
- flask
- flask-cors

Opcional:

 - python-env
    - >sudo pip3 install virtualenv 

## Instalando

- Baixe o projeto

> git clone https://github.com/cmagnobarbosa/SimpleRest.git

- Crie um ambiente virtual:
> python3 -m venv ambiente

- Ative o ambiente virtual:
> source ambiente/bin/activate

- Acesse o diretório SimpleRest

> pip install -r requirements.txt

- Execute

>python main.py

Carlos Magno 2019