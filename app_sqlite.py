"""
Avaliação – Python + SQLite
Tema: CRUD em 'alunos'

O que o script deve fazer:
1) Criar 'escola.db'
2) Criar tabela 'alunos' -> Seguindo o diagrama
3) Inserir registros na tabela alunos
4) Listar todos
5) Buscar por id
6) Atualizar registros
7) Deletar registros

"""

import sqlite3


conexao = sqlite3.connect("./escola.db")


conexao.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER,
        email TEXT NOT NULL UNIQUE
    )
""")


conexao.execute("""
    INSERT OR IGNORE INTO alunos (nome, idade, email)
    VALUES ('João Pereira', 18, 'joao.pereira@gmail.com')
""")
conexao.commit()

# Lista todos os alunos
lista_alunos = conexao.execute("SELECT * FROM alunos").fetchall()
print("Lista de alunos:", lista_alunos)

# Busca aluno pelo ID
aluno_id_1 = conexao.execute("SELECT * FROM alunos WHERE id = 1").fetchall()
print("Aluno com ID 1:", aluno_id_1)

# Atualiza o nome do aluno com ID 1
conexao.execute("""
    UPDATE alunos
    SET nome = 'João P. Silva'
    WHERE id = 1
""")
conexao.commit()

# Verifica a atualização
aluno_atualizado = conexao.execute("SELECT * FROM alunos WHERE id = 1").fetchall()
print("Aluno atualizado:", aluno_atualizado)

# Deleta o aluno com ID 1
conexao.execute("DELETE FROM alunos WHERE id = 1")
conexao.commit()