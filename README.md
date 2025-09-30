# ⚙️ Projeto T2: CRUD Manager em Python com Persistência JSON

Este projeto implementa um **Sistema de Gerenciamento de Registros (CRUD)** completo, desenvolvido em Python, com o objetivo de demonstrar a manipulação de dados persistidos em arquivos do tipo **JSON**. O sistema é estruturado em classes para garantir a separação de responsabilidades e a legibilidade do código.

---

## ✨ Funcionalidades

O projeto atende aos requisitos do trabalho T2, implementando o ciclo completo de operações de dados:

| Operação | Método | Descrição |
| :--- | :--- | :--- |
| **CREATE** | `add_record()` | Cadastra um novo registro e atribui um ID único. |
| **READ** | `get_record_by_id()` | Busca e exibe um registro específico pelo seu ID. |
| **READ** | `list_all_records()` | Lista todos os registros armazenados no sistema. |
| **UPDATE** | `update_record()` | Atualiza os dados de um registro existente através do seu ID. |
| **DELETE** | `delete_record()` | Exclui permanentemente um registro pelo seu ID. |

---

## 🎯 Estrutura do Projeto

O código é dividido em módulos para seguir as boas práticas de programação modular e Orientação a Objetos.

### 1. `main.py`
É o ponto de entrada do programa, responsável pela interface do usuário (menu e I/O).

### 2. `utils/CRUDManager.py`
Contém a **lógica de negócios** (as funções CRUD) e gerencia a lista de registros em memória.

### 3. `utils/FileManager.py`
Responsável unicamente pela **persistência** (leitura e escrita) dos dados no arquivo JSON.

---

## 🚀 Como Executar o Projeto

1. **Pré-requisitos:** Certifique-se de ter o Python 3 instalado.
2. **Organização:** Certifique-se de que os arquivos `.py` estão nas pastas corretas (`FileManager.py` e `CRUDManager.py` devem estar dentro da pasta `utils`).
3. **Inicie o Sistema:** Navegue até o diretório principal do projeto (`/Python-CRUD-JSONDATA`) e execute:

```bash
python main.py