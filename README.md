# ArretadoShop 🛒

**ArretadoShop** é um sistema de vendas fullstack web desenvolvido com Python, focado no aprendizado prático de desenvolvimento de APIs REST com FastAPI, banco de dados com SQLAlchemy, autenticação, front-end básico e deploy. O projeto visa criar uma aplicação realista e escalável para gerenciar produtos, pedidos e usuários.

---

## 📌 Sumário

- [Tecnologias](#-tecnologias)  
- [Funcionalidades](#-funcionalidades)  
- [Estrutura do Projeto](#-estrutura-do-projeto)  
- [Instalação](#-instalação)  
- [Como Rodar](#-como-rodar)  
- [Uso](#-uso)  
- [Contribuição](#-contribuição)  
- [Licença](#-licença)  
- [Contato](#-contato)  

---

## 🛠 Tecnologias

| Camada          | Tecnologias                             |
|-----------------|---------------------------------------|
| Backend         | Python 3.10+, FastAPI, SQLAlchemy     |
| Banco de Dados  | SQLite (local) / PostgreSQL (prod)    |
| Validação       | Pydantic                              |
| Front-end       | HTML5, CSS3, JavaScript (básico)      |
| Controle de Versão | Git, GitHub                        |
| Deploy          | Railway (backend), Vercel (frontend)  |

---

## 🚀 Funcionalidades

- Cadastro e autenticação segura de usuários (JWT)  
- CRUD completo de produtos e pedidos  
- Validação rigorosa de dados com Pydantic  
- Interface front-end simples para cadastro e visualização  
- Documentação automática via Swagger UI  
- Estrutura escalável e modular  
- Testes automatizados para as principais funcionalidades  

---

## 📁 Estrutura do Projeto

arretadoshop/
│
├── app/
│ ├── main.py # Entrada da aplicação FastAPI
│ ├── routers/ # Rotas organizadas por funcionalidade
│ ├── models/ # Modelos SQLAlchemy do banco de dados
│ ├── schemas/ # Schemas Pydantic para validação
│ ├── core/ # Configurações e segurança (autenticação)
│ ├── database.py # Configuração da conexão com o banco
│ └── utils/ # Funções auxiliares e helpers
│
├── tests/ # Testes unitários e de integração
├── venv/ # Ambiente virtual (ignorando no git)
├── .gitignore # Arquivos e pastas ignorados pelo git
├── requirements.txt # Dependências do projeto
├── README.md # Documentação do projeto
└── LICENSE # Licença do projeto


---

## ⚙️ Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/arretadoshop.git
cd arretadoshop
python3 -m venv venv
source venv/bin/activate      # Linux / macOS / Git Bash
# Ou no Windows (cmd):
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
