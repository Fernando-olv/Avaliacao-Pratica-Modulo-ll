import sqlite3
conn = sqlite3.connect("escola.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    email TEXT
    )
""")

cursor.execute("INSERT INTO alunos(nome, idade, email)VALUES(?,?,?)",
               ("Emily",17,"emily@gmail.com"))
cursor.execute("INSERT INTO alunos(nome, idade, email)VALUES(?,?,?)",
               ("Luan",18,"luan@gmail.com"))
cursor.execute("INSERT INTO alunos(nome, idade, email)VALUES(?,?,?)",
               ("lucas",20,"lucas@gmail.com"))

cursor.execute("SELECT * FROM alunos")
for linha in cursor.fetchall():
    print (linha)

cursor.execute("UPDATE alunos SET email = ?  WHERE nome = ?",
               ("emilyaf@gmail.com", "Emily"))
conn.commit()


cursor.execute("DELETE FROM alunos WHERE nome = ?", ("Emily",))
conn.commit

conn.close()