# 🪨 SCP - Sistema de Controle de Pátio

Projeto de Backend API desenvolvido para o curso **Programador de Sistemas** do **Senac**.

O objetivo deste projeto é construir uma API 100% funcional (Backend) para o gerenciamento de um pátio de Mármore e Granito.

Este repositório contém todo o progresso do curso, desde os algoritmos iniciais em VisualG (UC1) até a API final em Python + Flask conectada a um banco de dados real (UC2).

## ✨ Funcionalidades Principais (Endpoints da API)

O objetivo final é construir endpoints CRUD (Create, Read, Update, Delete) para as seguintes entidades do sistema:

* [ ] API CRUD: **Materiais** (Ex: "Amarelo Ornamental", "Verde Ubatuba")
* [ ] API CRUD: **Blocos** (O bloco físico de pedra no pátio, com código, dimensões, material, etc.)
* [ ] API CRUD: **Clientes** (As marmorarias ou clientes que compram os blocos)
* [ ] API CRUD: **Pedidos** (O registro de venda de um ou mais blocos para um cliente)

## 🛠️ Tecnologias Utilizadas

Esta é a "stack" de tecnologia definida em nosso plano de curso:

* **Lógica:** VisualG
* **Linguagem:** Python
* **Framework Backend:** Flask
* **Banco de Dados:** MySQL
* **Ferramentas de Desenvolvimento:** VS Code, Git/GitHub
* **Ambiente Python:** `venv` (Ambiente Virtual)
* **Testes de API:** Insomnia / Postman

## 🚀 Como Rodar o Projeto (Guia para Alunos)

Instruções rápidas para rodar o projeto **Backend (API)** final:

1.  Clone o repositório:
    ```bash
    git clone [URL_DO_SEU_REPO]
    cd scp-backend
    ```
2.  Crie e ative o ambiente virtual (`venv`):
    ```bash
    # No Mac/Linux
    python3 -m venv .venv
    source .venv/bin/activate

    # No Windows
    python -m venv .venv
    .\.venv\Scripts\activate
    ```
3.  Instale as dependências do Python:
    ```bash
    pip install -r requirements.txt
    ```
4.  Configure o Banco de Dados MySQL:
    * Crie um banco de dados local (ex: `scp_db`).
    * Importe a estrutura das tabelas (o arquivo `/sql/schema.sql`) no seu MySQL.
    * Renomeie o arquivo `.env.example` para `.env` e ajuste as credenciais (DB_USER, DB_PASS).
5.  Execute a aplicação Flask:
    ```bash
    flask run
    ```
6.  Teste a API:
    * Abra o Insomnia (ou Postman).
    * Faça uma requisição `GET` para `http://127.0.0.1:5000/api/materiais` para ver se a conexão funciona.

## 📝 Licença

Este projeto utiliza a Licença MIT.

Joao Vitor Tulli Ribeiro