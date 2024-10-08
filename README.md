# Taskmanager-Terminal

## Descrição

Este é um gerenciador de tarefas simples, desenvolvido em Python, que permite aos usuários adicionar, editar, remover e visualizar suas tarefas. O aplicativo utiliza um banco de dados SQLite3 para armazenar as informações das tarefas.

## Como usar

1. **Instalação:**
   * **Criar um ambiente virtual (recomendado):**

     ```bash
     python -m venv venv
     ```

     * **Ativar o ambiente virtual:**
       * **Windows:** `venv\Scripts\activate`
       * **Linux/macOS:** `source venv/bin/activate`
   * **Instalar as dependências:**

     ```bash
     pip install -r requirements.txt
     ```
2. **Executar o aplicativo:**
   ```bash
   python app.py
   ```

## Funcionalidades

O aplicativo oferece as seguintes funcionalidades:

* **Adicionar Tarefa:** Permite adicionar novas tarefas ao banco de dados.
* **Editar Tarefa:** Permite modificar o texto de uma tarefa existente.
* **Remover Tarefa:** Permite excluir uma tarefa do banco de dados.
* **Visualizar Tarefas:** Mostra todas as tarefas armazenadas.

## Interface do Usuário

Ao iniciar o aplicativo, você verá o seguinte menu:

```
Table 'text' created successfully
1: Add Task
2: Edit Task
3: Remove Task
4: View Tasks
5: Exit
Type here:
```

* **1: Add Task:** Digite o texto da tarefa e pressione Enter.
* **2: Edit Task:** Digite o ID da tarefa que deseja editar e o novo texto.
* **3: Remove Task:** Digite o ID da tarefa que deseja remover.
* **4: View Tasks:** Mostra uma lista de todas as tarefas com seus respectivos IDs.
* **5: Exit:** Encerra o aplicativo.

## Estrutura do Projeto

* **app.py:** Ponto de entrada do aplicativo.
* **db_utils.py:** Contém funções para interagir com o banco de dados SQLite3.
* **scr.py:** Contém a lógica para a interface do usuário e as funcionalidades do aplicativo.
* **data.db:** Arquivo do banco de dados.
* **requirements.txt:** Lista as dependências do projeto.

## Contribuições

Contribuições são bem-vindas! Para contribuir, por favor, siga as seguintes etapas:

1. Fork este repositório.
2. Crie um novo branch para sua feature.
3. Faça as suas alterações e commit.
4. **Envie um pull request.**
