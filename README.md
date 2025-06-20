# Django React TodoList
## Este projeto é uma aplicação de lista de tarefas (Todo List) desenvolvida utilizando Django no backend e React no frontend. O objetivo é fornecer uma ferramenta simples e moderna para organização de tarefas, utilizando uma arquitetura full-stack robusta e escalável.

## Funcionalidades
- ✅ Cadastro, edição e remoção de tarefas
- ✅ Marcar tarefas como concluídas ou pendentes
- ✅ Interface intuitiva e responsiva
- ✅ Integração entre backend (Django) e frontend (React) via API REST
- ✅ Persistência dos dados em banco de dados relacional

## Tecnologias Utilizadas
- Backend
  - Django — Framework web em Python
  - Django REST Framework — Criação de APIs RESTful
- Frontend
  - React — Biblioteca JavaScript para interfaces de usuário
  - Axios — Requisições HTTP para integração com a API
- Outras
 - HTML, CSS, JavaScript

### Como Executar o Projeto
Pré-requisitos:
- Python 3.x
- Node.js e npm/yarn

### Passos
Clone o repositório

```bash
git clone https://github.com/Cauanz/django-react-todolist.git
cd django-react-todolist
```

Instale as dependências do backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Instale as dependências do frontend
```bash
cd ../frontend
npm install
npm start
Acesse a aplicação em http://localhost:3000 (frontend)
O backend estará disponível em http://localhost:8000
```

Estrutura do Projeto
```Code
django-react-todolist/
├── backend/          # Código do Django (API)
│   └── ...
├── frontend/         # Código do React
│   └── ...
└── README.md
```

Licença
Este projeto está sob a licença MIT.
