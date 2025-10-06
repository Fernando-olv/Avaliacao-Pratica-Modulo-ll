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

conexao.execute("CREATE TABLE IF NOT EXISTS alunos (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER,email TEXT)")

conexao.execute("INSERT INTO alunos (nome ,idade,email)VALUES ('ANA MARIA',18,'anamaria@gmail.com')")

conexao.commit()

conexao.execute("INSERT INTO alunos(nome, idade, email) VALUES ('ANA ', 16, 'ANA.MARIA1@gmail.com')")
conexao.commit()
print(conexao.execute("SELECT *  FROM alunos").fetchall())

print(conexao.execute('SELECT * FROM alunos WHERE id= 1'))

##6 Atualizar Registro
conexao.execute("UPDATE alunos SET nome='JOAO' WHERE id=1")
conexao.commit()

conexao.execute("DELETE FROM alunos WHERE id=1")
conexao.commit()