# Teste Contato Seguro - Backend

## API desenvolvida para um teste técnico da Contato Seguro. Ela cadastra usuários e empresas e cria uma relana N -> N entre essas entidades

# Tecnologias utilizadas

![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Flask-migrate](https://img.shields.io/badge/flask--migrate-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Flask-sqlalchemy](https://img.shields.io/badge/flask--sqlalchemy-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

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
