# 📘 Avaliação – Desenvolvimento com Python

Essa avalição é dividida em **2 partes**:

1. **API REST Calculadora com Flask**  
2. **CRUD em Banco de Dados SQLite**

---

## 🔹 Parte 1 – API REST Calculadora com Flask

### 🎯 Critérios de Correção
- Criar uma aplicação **Flask** básica.  
- Implementar **rotas** que recebem parâmetros pela URL.  
- Retornar resultados em **formato JSON**.

---

### 🚀 Instruções

#### 1. Estrutura inicial
Você já tem o arquivo `app.py` com o seguinte código:

```python
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
```

#### 2. Criando as rotas da calculadora
Implemente **4 rotas GET** que recebem parâmetros pela URL e retornam JSON com o resultado:

- `/soma?valor1=5&valor2=6`  
- `/subtrair?valor1=5&valor2=6`  
- `/multiplicar?valor1=5&valor2=6`  
- `/dividir?valor1=5&valor2=6`

👉 **Dicas:**
- Use `request.args.get("valor1")` para capturar parâmetros.  
- Converta valores com `float()`.  
- Retorne um dicionário Python (Flask converte para JSON).  

#### 3. Tratando erros
Na divisão, evite erro de divisão por zero.  
👉 Exemplo:
```python
if v2 == 0:
    return {"erro": "Divisão por zero não é permitida"}
```

---

### 📌 Checklist
- [ ] Implementar rota `/soma`.  
- [ ] Implementar rota `/subtrair`.  
- [ ] Implementar rota `/multiplicar`.  
- [ ] Implementar rota `/dividir` (tratando divisão por zero).  
- [ ] Testar as rotas no navegador ou no **Postman/requests**.  

---

### 🧪 Testando
Rodando o projeto (`python app.py`), abra no navegador:

- [http://127.0.0.1:5000/soma?valor1=10&valor2=20]

Retorno esperado:
```json
{"resultado": 30.0}
```

---

## 🔹 Parte 2 – CRUD com Python e SQLite

### 🎯 Critérios de Correção
O script deve implementar as operações **CRUD** na tabela `alunos`.

---

### 📌 Checklist

#### 1) Criar banco de dados  
- [X] Criou o banco `escola.db` usando `sqlite3.connect()`.  
- [X] Conexão e cursor foram criados corretamente.  

#### 2) Criar tabela `alunos`  
- [ X ] Usou `CREATE TABLE`
- [ X ] Seguiu o diagrama especificado (`id`, `nome`, `idade`, `email`).  
- [ X ] Definiu `id` como **PRIMARY KEY**.  
- [ X ] Respeitou os tipos corretos (TEXT, INTEGER, etc.).  

#### 3) Inserir registros  
- [ ] Usou `INSERT INTO alunos (...) VALUES (?, ?, ?)` com parâmetros.  
- [ ] Inseriu pelo menos 2 ou 3 registros de exemplo.   

#### 4) Listar todos  
- [ ] Usou `SELECT * FROM alunos`.  
- [ ] Exibiu os registros no console.  

#### 5) Buscar por ID  
- [ ] Criou consulta `SELECT * FROM alunos WHERE id = ?`.  
- [ ] Exibiu corretamente o resultado da busca.  

#### 6) Atualizar registros  
- [ ] Usou `UPDATE alunos SET ... WHERE id = ?`.  
- [ ] Fez `conn.commit()` após atualização.  
- [ ] Mostrou o registro atualizado no console.  

#### 7) Deletar registros  
- [ ] Usou `DELETE FROM alunos WHERE id = ?`.  
- [ ] Fez `conn.commit()` após exclusão.  
- [ ] Confirmou a exclusão listando os registros restantes.  

---
