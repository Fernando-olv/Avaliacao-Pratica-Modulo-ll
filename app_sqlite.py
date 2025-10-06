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

## 1 - Criação do banco
conexao = sqlite3.connect("./escola.db")
# 2 - Criação da tabela
conexao.execute("CREATE TABLE IF NOT EXISTS alunos (id INTEGER PRIMARY KEY,nome TEXT,idade INTERGER,email TEXT)")
# 3 - Inserção de dados
conexao.execute("INSERT INTO alunos (nome, idade, email) VALUES ('LEONARDO',20, 'leonardo@gmail.com')"),
conexao.commit()
#4 - Seleção dos dados
print(conexao.execute("select * FROM alunos").fetchall())
#5 - Update
conexao.execute ("UPDATE alunos SET email = 'superemail@gmail.com' WHERE id=1")
conexao.commit()

print(conexao.execute("select * FROM alunos").fetchall())
#7- delete 
conexao.execute("DELETE FROM alunos WHERE id =1 ")

