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

def conexao_banco():
    conexao = sqlite3.connect("escola.db")
    return conexao




with conexao_banco() as banco:
    banco.execute("CREATE TABLE IF NOT EXISTS alunos (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER, email TEXT NOT NULL)")




with conexao_banco() as banco:
    banco.execute("INSERT INTO alunos (nome, idade, email) VALUES ('Luiz Antônio', 15, 'luizsafadao4324@hotmail.com')")




with conexao_banco() as banco:
    banco.execute("SELECT * FROM alunos").fetchall()



with conexao_banco() as banco:
    banco.execute("SELECT * FROM alunos WHERE id = ?", (1,)).fetchall()




with conexao_banco() as banco:
    banco.execute("UPDATE alunos SET nome = ?, idade = ? WHERE id = ?", ("Luiz A.", 15, 1))




with conexao_banco() as banco:
    banco.execute("DELETE FROM alunos WHERE id = 1")