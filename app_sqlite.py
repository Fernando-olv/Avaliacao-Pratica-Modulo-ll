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

## 1 - Criar escola.db
def conexao_banco():
    conexao = sqlite3.connect("escola.db")
    return conexao 

## 2 - Criar tabela alunos --> seguindo o diagrama 
with conexao_banco() as conexao:
    conexao.execute("CREATE TABLE IF NOT EXISTS alunos (id INTEGER PRIMARY KEY, nome TEXT, materia TEXT, data_nascimento DATE)")

## 3 - Inserir Registros na tabela alunos 
with conexao_banco() as conexao:
    conexao.execute(" INSERT INTO alunos (nome,materia,data_nascimento) VALUES ('Eike Vilela','Português','2009-08-18')")

## 4 - Listar todos 
with conexao_banco() as conexao:
    listar_alunos = conexao.execute("SELECT * FROM alunos").fetchall()
    print(listar_alunos)

## 5 - Buscar por id 
with conexao_banco() as conexao:
    id_alunos = conexao.execute("SELECT * FROM alunos WHERE id=4").fetchall()
    print(id_alunos)

## 6 - Atualizar Registros 
with conexao_banco() as conexao:
    conexao.execute("UPDATE alunos SET nome= 'Renan Romão' WHERE id = 1")

## 7 - Deletar Registros 
with conexao_banco() as conexao:
    conexao.execute("DELETE FROM alunos WHERE data_nascimento = '2008-06-07'")
    