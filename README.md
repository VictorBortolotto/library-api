# Library API

A **Library** é uma aplicação desenvolvida como **MVP (Minimum Viable Product)** para fins acadêmicos, no contexto de uma **Pós-Graduação em Engenharia de Software**.

O projeto tem como objetivo demonstrar, de forma prática, conceitos de arquitetura de software, comunicação entre APIs, persistência de dados, regras de negócio, comunicação via gRPC e integração com serviços externos.

> **Nota:** Este projeto possui finalidade **exclusivamente acadêmica e demonstrativa**. As funcionalidades, regras de negócio e decisões de arquitetura foram definidas para atender aos objetivos do MVP e **não representam necessariamente requisitos, regras ou necessidades de um sistema real de gerenciamento de bibliotecas**. O projeto não deve ser considerado uma solução pronta para utilização em ambiente de produção.

Este repositório contém a **Library API**, responsável pela implementação das **regras de negócio**, operações de **CRUD**, comunicação com o **banco de dados** e disponibilização dos serviços **gRPC** utilizados pela API Proxy.

---

# Arquitetura

A aplicação é composta por duas APIs:

* **Library Proxy API**: porta de entrada da aplicação, responsável pela autenticação, geração e validação de tokens JWT e encaminhamento das requisições.
* **Library API**: responsável pelas regras de negócio, operações de CRUD, acesso ao banco de dados e integração com serviços externos.

A comunicação entre as duas APIs é realizada utilizando **gRPC**.

```text
                    ┌──────────────────────┐
                    │       Cliente        │
                    └──────────┬───────────┘
                               │
                               │ HTTP
                               ▼
                    ┌──────────────────────┐
                    │  Library Proxy API   │
                    │      :8081           │
                    │                      │
                    │ • Autenticação       │
                    │ • JWT                │
                    │ • Validação          │
                    │ • Proxy              │
                    └──────────┬───────────┘
                               │
                               │ gRPC
                               ▼
                    ┌──────────────────────┐
                    │     Library API      │
                    │                      │
                    │ HTTP: :8080          │
                    │ gRPC: :50051         │
                    │                      │
                    │ • Regras de negócio  │
                    │ • CRUD               │
                    │ • Banco de dados     │
                    │ • Serviços externos  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       SQLite         │
                    └──────────────────────┘
```

---

# Funcionalidades

### Usuários

* Criação de usuários
* Processo de login

### Clientes

* Cadastro de clientes
* Atualização de clientes
* Desativação de clientes

### Livros

* Cadastro de livros
* Atualização de livros
* Consulta de livros
* Exclusão de livros

### Empréstimos

* Cadastro de empréstimos de livros
* Atualização de empréstimos
* Consulta de empréstimos

### Integrações

* Comunicação com a **Library Proxy API** utilizando gRPC
* Consulta de informações de CEP através de serviço externo

---

# Tecnologias utilizadas

* **Python**
* **Flask** — desenvolvimento da API HTTP
* **SQLite** — banco de dados
* **gRPC** — comunicação com a API Proxy
* **Docker** — containerização da aplicação
* **Docker Compose** — gerenciamento do container
* **Swagger** — documentação da API

---

# Como executar o projeto

Existem duas formas de executar a aplicação:

1. Utilizando **Docker**
2. Executando diretamente no ambiente local

> Para utilizar a aplicação completa, a **Library Proxy API** também deverá estar em execução, pois ela é responsável por receber as requisições dos clientes e se comunicar com esta API através do gRPC.

---

# Executando com Docker

## Pré-requisitos

Antes de iniciar, certifique-se de possuir instalado:

* Docker
* Docker Compose

## 1. Clonar o repositório

```bash
git clone https://github.com/VictorBortolotto/library-api.git
```

## 2. Acessar a pasta do projeto

```bash
cd library-api
```

## 3. Acessar a pasta do Docker

```bash
cd docker
```

## 4. Criar a network do Docker

Antes de iniciar o container, é necessário criar a rede utilizada pela aplicação:

```bash
docker network create library-network
```

> Caso a network já exista, não é necessário executar esse comando novamente.

## 5. Construir e iniciar o container

```bash
docker compose up --build
```

Após a inicialização, a aplicação estará disponível na porta **8080** para HTTP e na porta **50051** para gRPC.

Uma saída semelhante à seguinte deverá ser apresentada:

```text
library-api  | Porta configurada: 50051
library-api  | Servidor gRPC iniciado em localhost:50051
library-api  | * Serving Flask app 'br.com.app.src.main.Main'
library-api  | * Debug mode: off
library-api  | WARNING: This is a development server. Do not use it in a production deployment.
library-api  | * Running on all addresses (0.0.0.0)
library-api  | * Running on http://127.0.0.1:8080
library-api  | * Running on http://172.19.0.2:8080
library-api  | Press CTRL+C to quit
```

A API HTTP estará disponível em:

```text
http://localhost:8080
```

O servidor gRPC estará disponível na porta:

```text
localhost:50051
```

Para interromper o container:

```bash
docker compose down
```

---

# Executando sem Docker

Também é possível executar a aplicação diretamente no ambiente local.

## 1. Clonar o repositório

```bash
git clone https://github.com/VictorBortolotto/library-api.git
```

## 2. Acessar a pasta do projeto

```bash
cd library-api
```

## 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

## 4. Acessar a pasta principal da aplicação

```bash
cd br/com/app/src/main
```

## 5. Iniciar a aplicação

```bash
flask --app Main run -p 8080
```

Após iniciar, deverá ser apresentada uma saída semelhante a:

```text
Porta configurada: 50051
Servidor gRPC iniciado em localhost:50051
* Serving Flask app 'Main'
* Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment.
* Running on http://127.0.0.1:8080
Press CTRL+C to quit
```

A API HTTP estará disponível em:

```text
http://localhost:8080
```

E o servidor gRPC estará disponível em:

```text
localhost:50051
```

---

# Banco de dados

A aplicação utiliza **SQLite** como banco de dados.

O banco de dados é **gerado automaticamente durante a inicialização da aplicação**, incluindo a criação das tabelas necessárias para o funcionamento do sistema.

Não é necessário executar scripts SQL manualmente para criar a estrutura inicial do banco.

O arquivo do banco de dados é armazenado dentro da estrutura de diretórios da aplicação.

---

# Regeneração dos arquivos gRPC

Os arquivos Python utilizados pelo gRPC são gerados a partir dos arquivos `.proto` localizados em:

```text
br/com/app/src/main/proto
```

Caso seja necessário regenerar os arquivos presentes na pasta `generated`, execute os comandos abaixo a partir da raiz do projeto.

### Book Loan

```bash
python -m grpc_tools.protoc -I=br/com/app/src/main/proto --python_out=br/com/app/src/main/generated --grpc_python_out=br/com/app/src/main/generated br/com/app/src/main/proto/book_loan.proto
```

### Book

```bash
python -m grpc_tools.protoc -I=br/com/app/src/main/proto --python_out=br/com/app/src/main/generated --grpc_python_out=br/com/app/src/main/generated br/com/app/src/main/proto/book.proto
```

### Client

```bash
python -m grpc_tools.protoc -I=br/com/app/src/main/proto --python_out=br/com/app/src/main/generated --grpc_python_out=br/com/app/src/main/generated br/com/app/src/main/proto/client.proto
```

### User

```bash
python -m grpc_tools.protoc -I=br/com/app/src/main/proto --python_out=br/com/app/src/main/generated --grpc_python_out=br/com/app/src/main/generated br/com/app/src/main/proto/user.proto
```

### Zip Code

```bash
python -m grpc_tools.protoc -I=br/com/app/src/main/proto --python_out=br/com/app/src/main/generated --grpc_python_out=br/com/app/src/main/generated br/com/app/src/main/proto/zip_code.proto
```

---

# Ajuste dos imports dos arquivos gerados

Dependendo da versão do `grpc_tools` e da estrutura do projeto, pode ser necessário ajustar os imports dos arquivos `*_pb2_grpc.py` gerados.

Por exemplo, caso o arquivo seja gerado com:

```python
import zip_code_pb2 as zip__code__pb2
```

altere para:

```python
from generated import zip_code_pb2 as zip__code__pb2
```

Esse ajuste permite que o arquivo encontre corretamente o módulo `zip_code_pb2` dentro do pacote `generated`.

---

# Portas utilizadas

| Serviço           | Protocolo |   Porta |
| ----------------- | --------- | ------: |
| Library Proxy API | HTTP      |  `8081` |
| Library API       | HTTP      |  `8080` |
| Library API       | gRPC      | `50051` |

---

# Documentação da API

A aplicação possui documentação através do **Swagger**.

Após iniciar a aplicação, a documentação poderá ser acessada através da rota configurada para o Swagger.

> A URL exata da documentação depende da configuração atual do projeto.

---

# Observações

* A **Library API** é responsável pelas regras de negócio e persistência dos dados.
* O banco de dados utilizado é o **SQLite**.
* O banco e suas tabelas são criados automaticamente durante a inicialização da aplicação.
* A comunicação com a **Library Proxy API** é realizada através de **gRPC**.
* A API também realiza integração com serviço externo para consulta de informações de CEP.
* A porta HTTP utilizada pela API é `8080`.
* A porta utilizada pelo servidor gRPC é `50051`.
* Para utilizar a aplicação completa, a **Library Proxy API** e a **Library API** devem estar disponíveis.

---

<h2 align="start">Autor</h2>

<h2 style="border: none">Victor Augusto Campos Bortolotto</h2>
<img style="width: 100px; height: 100px" src="https://avatars.githubusercontent.com/u/50971139?v=4" alt=""/>

[![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/victor-augusto-campos-bortolotto/)](https://www.linkedin.com/in/victor-augusto-campos-bortolotto/) 
[![Gmail Badge](https://img.shields.io/badge/-victorcamposbortolottowork@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:victorcamposbortolottowork@gmail.com)](mailto:victorcamposbortolottowork@gmail.com)