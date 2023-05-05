# Teste Contato Seguro - Backend

## API desenvolvida para um teste técnico da Contato Seguro. Ela cadastra usuários e empresas e cria uma relana N -> N entre essas entidades

<br>

# Tecnologias utilizadas

[![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/2.3.x/)
[![Flask-migrate](https://img.shields.io/badge/flask--migrate-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)](https://flask-migrate.readthedocs.io/en/latest/)
[![Flask-sqlalchemy](https://img.shields.io/badge/flask--sqlalchemy-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/)
[![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)](https://jwt.io/)
[![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)](https://www.markdownguide.org/)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)

<br>

# Funcionalidades do projeto

- CRUD usuário
- CRUD empresa
- Vincular empresa a usuário
- Listar empresas vinculadas ao usuário

<br>

# 🎲 Rodando o Back End (servidor)

Você terá que criar o arquivo .env baseado no .env.example e por o url de um banco de dados postgres. Perceba que a url tem que começar com postgresql! Você talvez queira criar um ambiente virtual também.

```bash
# Clone este repositório
$ git clone https://github.com/Iago-pixel/teste-back-end-contato-seguro.git

# Acesse a pasta do projeto no terminal/cmd
$ cd teste-back-end-contato-seguro

# Instale as dependências
$ pip install -r requirements.txt

# Execute o migrete
$ flask db upgrade

# Execute a aplicação em modo de desenvolvimento
$ flask run

# O servidor inciará na porta:5000 - acesse http://localhost:5000
``
```

## Rotas

### **/user**

#### POST

```
{
    "name": "Ester",
    "email": "ester@test.com",
    "phone": "1111-1111",
    "birth": "26/12/2002",
    "city": "Natal"
}
```

<br>

[![CREATED badge](https://img.shields.io/badge/CREATED-201-<COLOR>.svg)](https://shields.io/)

```
{
	"id": 7,
	"name": "Ester",
	"email": "ester@test.com",
	"phone": "1111-1111",
	"birth": "26/12/2002",
	"city": "Natal",
	"companies": []
}
```

<br>

#### GET

```

```

<br>

[![OK badge](https://img.shields.io/badge/OK-200-<COLOR>.svg)](https://shields.io/)

```
[
	{
		"id": 6,
		"name": "Iago",
		"email": "iago@test.com",
		"phone": "0000-0000",
		"birth": "25/08/2002",
		"city": "Natal"
	},
	{
		"id": 7,
		"name": "Ester",
		"email": "ester@test.com",
		"phone": "1111-1111",
		"birth": "26/12/2002",
		"city": "Natal"
	}
]
```

### **/user/<user_id>**

#### **GET**

```

```

<br>

[![OK badge](https://img.shields.io/badge/OK-200-<COLOR>.svg)](https://shields.io/)

```
{
	"id": 7,
	"name": "Ester",
	"email": "ester@test.com",
	"phone": "1111-1111",
	"birth": "26/12/2002",
	"city": "Natal"
}
```

<br>

[![NOT FOUND badge](https://img.shields.io/badge/NOT%20FOUND-404-orange.svg)](https://shields.io/)

```
<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>Usuário não encontrado</p>
```

#### **PATCH**

```
{
    "phone": "1111-1112"
}
```

<br>

[![NO CONTENT badge](https://img.shields.io/badge/NO%20CONTENT-204-<COLOR>.svg)](https://shields.io/)

```

```

<br>

[![NOT FOUND badge](https://img.shields.io/badge/NOT%20FOUND-404-orange.svg)](https://shields.io/)

```
<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>Usuário não encontrado</p>
```

<br>

#### **DELETE**

```

```

<br>

[![NO CONTENT badge](https://img.shields.io/badge/NO%20CONTENT-204-<COLOR>.svg)](https://shields.io/)

```

```

<br>

[![NOT FOUND badge](https://img.shields.io/badge/NOT%20FOUND-404-orange.svg)](https://shields.io/)

```
<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>Usuário não encontrado</p>
```

<br>

### **/user/<user_id>/<company_id>**

#### **PATCH**

```

```

<br>

[![NO CONTENT badge](https://img.shields.io/badge/NO%20CONTENT-204-<COLOR>.svg)](https://shields.io/)

```

```

<br>

[![NOT FOUND badge](https://img.shields.io/badge/NOT%20FOUND-404-orange.svg)](https://shields.io/)

```
<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>Usuário não encontrado</p>
```

<br>

[![NOT FOUND badge](https://img.shields.io/badge/NOT%20FOUND-404-orange.svg)](https://shields.io/)

```
<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>Empresa não encontrada</p>
```

<br>

### **/user/<user_id>/companies**

#### **GET**

```

```

<br>

[![OK badge](https://img.shields.io/badge/OK-200-<COLOR>.svg)](https://shields.io/)

```
[
	{
		"id": 5,
		"name": "Netflox",
		"cnpj": "1564546",
		"address": "rua da dona charopinha n 222"
	},
	{
		"id": 4,
		"name": "iFeed",
		"cnpj": "4232423",
		"address": "rua das marocas n 111"
	}
]
```

<br>

[![NOT FOUND badge](https://img.shields.io/badge/NOT%20FOUND-404-orange.svg)](https://shields.io/)

```
<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>Usuário não encontrado</p>
```

<br>

### **/company**

#### **POST**

```
{
	"name": "Netflox",
	"cnpj": "1564546",
	"address": "rua da dona charopinha n 222"
}
```

<br>

[![OK badge](https://img.shields.io/badge/OK-200-<COLOR>.svg)](https://shields.io/)

```
{
	"id": 5,
	"name": "Netflox",
	"cnpj": "1564546",
	"address": "rua da dona charopinha n 222"
}
```

<br>

#### **GET**

```

```

<br>

[![OK badge](https://img.shields.io/badge/OK-200-<COLOR>.svg)](https://shields.io/)

```
[
	{
		"id": 4,
		"name": "iFeed",
		"cnpj": "4232423",
		"address": "rua das marocas n 111"
	},
	{
		"id": 5,
		"name": "Netflox",
		"cnpj": "1564546",
		"address": "rua da dona charopinha n 222"
	}
]
```

<br>

### **/user/<company_id>**

#### **GET**

```

```

<br>

[![OK badge](https://img.shields.io/badge/OK-200-<COLOR>.svg)](https://shields.io/)

```
{
	"id": 5,
	"name": "Netflox",
	"cnpj": "1564546",
	"address": "rua da dona charopinha n 222"
}
```

<br>

[![NOT FOUND badge](https://img.shields.io/badge/NOT%20FOUND-404-orange.svg)](https://shields.io/)

```
<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>Empresa não encontrada</p>
```

<br>

#### **PATCH**

```
{
	"address": "rua da dona charopinha n 333"
}
```

<br>

[![OK badge](https://img.shields.io/badge/OK-200-<COLOR>.svg)](https://shields.io/)

```
{
	"id": 5,
	"name": "Netflox",
	"cnpj": "1564546",
	"address": "rua da dona charopinha n 333"
}
```

<br>

[![NOT FOUND badge](https://img.shields.io/badge/NOT%20FOUND-404-orange.svg)](https://shields.io/)

```
<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>Empresa não encontrada</p>
```

<br>

#### **DELETE**

```

```

<br>

[![NO CONTENT badge](https://img.shields.io/badge/NO%20CONTENT-204-<COLOR>.svg)](https://shields.io/)

```

```

<br>

[![NOT FOUND badge](https://img.shields.io/badge/NOT%20FOUND-404-orange.svg)](https://shields.io/)

```
<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>Empresa não encontrada</p>
```
