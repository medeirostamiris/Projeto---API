# Projeto API de Gerenciamento de Itens

Uma aplicação web simples desenvolvida com Flask seguindo o padrão MVC, criada para gerenciar itens, permitindo cadastrar, listar, editar, excluir e alterar o status. O sistema funciona integrado a uma API REST, conforme a rubrica da disciplina.

## Objetivo do Sistema

Oferecer um sistema intuitivo e funcional que permita ao usuário:

* Cadastrar itens de forma rápida
* Visualizar todos os itens em um só lugar
* Editar ou excluir informações
* Alterar o status dos itens
* Facilitar a organização das tarefas

## Público-Alvo

Qualquer pessoa que precise de uma ferramenta simples para organizar tarefas e informações, especialmente:

* Estudantes
* Pessoas com rotinas intensas
* Usuários que desejam uma solução prática

## Funcionalidades

* Criar itens
* Listar itens
* Editar itens
* Excluir itens
* Alterar status
* Filtrar por tipo e status
* Consumo de API
* Feedback visual (erro, sucesso e carregamento)

## Tecnologias Utilizadas

* Python 3
* Flask
* Jinja2 (templates)
* HTML + CSS
* JavaScript
* Tailwind CSS
* Estrutura MVC
* API REST
* SQLite / JSON (persistência)

## Arquitetura MVC

O projeto segue o padrão Model–View–Controller:

* **Model:** Camada responsável pelos dados e persistência (JSON ou SQLite).
* **View:** Interface localizada em 'frontend/', responsável pela interação com o usuário.
* **Controller:** Arquivos em 'controllers/' e 'routes/' responsáveis pelas rotas e regras de negócio.

## Estrutura do Projeto

```
Projeto---API/
├── backend/
│   ├── app.py
│   ├── controllers/
│   ├── models/
│   └── routes/
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
├── requirements.txt
├── README.md
└── Orientações do projeto.pdf
```

## Instalação

1. Clonar o repositório:

```sh
git clone https://github.com/medeirostamiris/Projeto---API.git
cd Projeto---API
```

2. Criar e ativar um ambiente virtual (Windows PowerShell):

```sh
python -m venv env
.\\env\\scripts\\activate
```

3. Instalar dependências:

```sh
pip install -r requirements.txt
```

## Executando a aplicação

1. Iniciar o backend:

```sh
cd backend
python app.py
```

2. Abrir o frontend:

Abra o arquivo `frontend/index.html` no navegador ou utilize a extensão Live Server.

A API estará disponível em:

```
http://localhost:5000
```

## Endpoints da API

### Listar Itens

```
GET /items
```

### Criar Item

```
POST /items
```

Body:

```json
{
  "title": "Estudar API",
  "type": "tarefa",
  "status": "pendente"
}
```

### Editar Item

```
PUT /items/:id
```

### Alterar Status

```
PATCH /items/:id/status
```

Body:

```json
{
  "status": "concluido"
}
```

### Remover Item

```
DELETE /items/:id
```

## Validações e Tratamento de Erros

O sistema realiza as seguintes validações:

* Título com no mínimo 3 caracteres
* Tipo dentro da lista permitida
* Status dentro da lista permitida

Em caso de erro, o sistema retorna status 400 com mensagem em JSON.

Exemplo:

```json
{
  "error": "Título inválido"
}
```

## Persistência de Dados

Os dados são armazenados utilizando:

* Arquivo JSON (`items.json`) ou
* Banco de dados SQLite

Isso garante que as informações não sejam perdidas ao reiniciar o servidor.

## Evidências do Sistema

Abaixo estão exemplos de funcionamento do sistema:

* Tela principal do frontend
* Criação de item
* Edição de item
* Exclusão de item
* Testes via Postman/Insomnia

> Inserir aqui os prints reais do sistema funcionando.

## Reflexão Crítica

### 1. Sobre o problema

A dificuldade em organizar tarefas e informações é comum entre estudantes e profissionais. Um sistema centralizado facilita o controle e evita esquecimentos.

### 2. Por que um sistema web?

* Pode ser acessado em qualquer computador com navegador.
* Não exige instalação complexa.
* Facilita a integração entre frontend e backend.

Outras soluções possíveis:

* Aplicativos móveis
* Agendas físicas
* Planilhas

A solução web é mais acessível e multiplataforma.

### 3. Limites da solução

* Dados armazenados localmente
* Ausência de autenticação
* Sem sincronização em nuvem
* Recursos limitados de acessibilidade

### 4. Aprendizados

Durante o desenvolvimento, aprendemos:

* Criação e consumo de APIs REST
* Integração frontend/backend
* Validação e tratamento de erros
* Persistência de dados
* Organização em MVC
* Trabalho em equipe

## Possíveis Melhorias (Bônus)

* Busca por texto no título
* Paginação ou ordenação
* Padronização de código (lint/format)
* Autenticação de usuários

## Integrantes do Grupo

* Emanoelly Francinny Brito Tavares
* Isabele Fernanda da Silva Albano
* Lívia Tainá de Medeiros Oliveira
* Tamíris dos Santos Medeiros

## Observações Finais

Este projeto foi desenvolvido seguindo a rubrica de avaliação da disciplina, atendendo aos critérios de API, frontend, persistência, documentação e evidências.
