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
##criaçao do banco 
conexao = sqlite3.connect("./escola.db")
##criação da tabela
conexao.execute("CREATE TABLE IF NOT EXISTS alunos(id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER, email TEXT)")
## Inserir dados na tabela
conexao.execute("INSERT INTO alunos (nome, idade, email) VALUES ('Gabriela', 20, 'gabi@gmail.com')")
conexao.commit()
print(conexao.execute("SELECT * FROM alunos").fetchall())
print(conexao.execute("SELECT * FROM alunos WHERE id = 5").fetchall())
##atualizar registros
conexao.execute("UPDATE alunos SET nome='Joana' WHERE id =6 ")
print(conexao.execute("SELECT * FROM alunos").fetchall())
##deletar
conexao.execute("DELETE FROM alunos WHERE id = 7")