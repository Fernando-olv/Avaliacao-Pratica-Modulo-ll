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

conexao.execute("CREATE TABLE if not exists alunos (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER, email TEXT NOT NULL UNIQUE)")

conexao.execute("INSERT OR IGNORE INTO alunos(nome,idade,email) values ('João Pereira',18,'joaozinho@gmail.com')")

conexao.commit()

#lista a lista
mos = conexao.execute("SELECT * FROM alunos").fetchall()

print (mos)
#busca id
bus_id = conexao.execute("SELECT * FROM alunos WHERE id= 1 ").fetchall()
print(bus_id)

#Atualiza
conexao.execute("UPDATE alunos SET nome='joaozinhooo' WHERE id=1")
conexao.commit()
#busca o id atualizado
bus_id = conexao.execute("SELECT * FROM alunos WHERE id= 1 ").fetchall()
print(bus_id)
#deleta
conexao.execute("DELETE FROM alunos WHERE id=1  ")
conexao.commit()


