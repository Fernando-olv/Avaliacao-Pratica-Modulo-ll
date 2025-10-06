"""
Avaliação – Python + SQLite
Tema: CRUD em 'alunos'
"""
import sqlite3

#O que o script deve fazer:
#1) Criar 'escola.db'
 
def conectar_banco():
    conexao = sqlite3.connect("escola.db")
    return conexao

#2) Criar tabela 'alunos' -> Seguindo o diagrama

with conectar_banco() as professores:
    professores.execute("CREATE TABLE IF NOT EXISTS alunos (id INTEGER PRIMARY KEY, nome TEXT NOT NULL, idade INTERGER, email TEXT NOT NULL)")
    
#3) Inserir registros na tabela alunos

with conectar_banco() as professores:
    professores.execute("INSERT INTO alunos (nome, idade, email) VALUES ('Osvaldo', 12, 'omi@gmail.com')")

#4) Listar todos
with conectar_banco() as professores:
    professores.execute("SELECT * FROM alunos")

#5) Buscar por id

with conectar_banco() as professores:
    professores.execute("SELECT * FROM alunos WHERE id=2")

#6) Atualizar registros

with conectar_banco() as professores:
    professores.execute("UPDATE alunos SET nome='Rubens' WHERE id=1")

#7) Deletar registros

with conectar_banco() as professores:
    professores.execute('DELETE FROM alunos WHERE id=1')
