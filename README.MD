
# Sistema de Times de Futebol (Django)

Este projeto é uma aplicação web desenvolvida com **Django** que permite gerenciar times de futebol de forma simples e interativa.

---

## Funcionalidades

* Listagem de times em formato de cards
* Criação de novos times
* Edição de times existentes
* Exclusão de times
* Interface moderna com Bootstrap
* Alternância de fundo (gradiente ↔ imagem)
* Animação suave ao trocar o fundo

---

## Tecnologias utilizadas

* Python
* Django
* SQLite
* HTML5
* CSS3
* Bootstrap 5
* JavaScript

---

## Como executar o projeto

### 1. Clone o repositório

git clone [https://github.com/Kampos-DCBS/Adalep.git](https://github.com/Kampos-DCBS/Adalep.git)
cd Adalep

---

### 2. Crie e ative o ambiente virtual

python -m venv venv
venv\Scripts\activate

---

### 3. Instale as dependências

pip install > requirements.txt

---

### 4. Execute as migrações

python manage.py migrate

---

### 5. Crie um superusuário (opcional)

python manage.py createsuperuser

---

### 6. Inicie o servidor

python manage.py runserver

---

## Acessos

* Aplicação: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## Estrutura do projeto

```
times/
├── models.py
├── views.py
├── urls.py
├── templates/
│   └── times/
├── static/
│   └── times/
```

---

## Interface

O sistema apresenta:

* Cards estilizados para cada time
* Botões de ação (editar e excluir)
* Formulário dinâmico para criação
* Troca de tema com animação

---

## Objetivo

Este projeto foi desenvolvido com fins acadêmicos para praticar:

* Criação de aplicações com Django
* Manipulação de banco de dados (CRUD)
* Uso de templates
* Estilização com CSS e Bootstrap
* Interatividade com JavaScript

---

## Autor

Daniel Campos Indiano da Silva

---
