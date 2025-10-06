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
import _sqlite3

## 1 Criar escola.db
def conexao_banco():
    conexao =_sqlite3.connect("escola.db")
    return conexao

## 2 Crair tabela alunos --> seguindo o diagrama
with conexao_banco() as conexao:
    conexao.execute("CREATE TABLE IF NOT EXISTS alunos (id INTEGER PRIMARY KEY, nome TEXT, materia TEXT, data_nascimento DATE)")

## 3 Inserção de dados
with conexao_banco() as conexao:
    conexao.execute("INSERT INTO alunos (nome,materia,data_nascimento) VALUES ('Daniel sovado', 'ADM', '1850-12-31')")

## 4 Pegando dados 
with conexao_banco() as conexao:
    lista_alunos = conexao.execute("SELECT * FROM alunos").fetchall()
    print(lista_alunos)

## 5 Pegue os dados pelo id
with conexao_banco() as conexao:
    pessoa = conexao.execute("SELECT * FROM alunos WHERE id=2").fetchall()
    print(pessoa)

## 6 Atualizar registros
with conexao_banco() as banco:
    conexao.execute("UPDATE alunos SET nome='Rigoni Victor' WHERE id= 1")

## 7 Deletar 
with conexao_banco() as banco:
    conexao.execute("DELETE FROM alunos WHERE data_nascimento = '1999-08-27'")
    