# nome: João Victor Moglia Dantas  turma:manha
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/soma', methods=["GET"])
def soma():
    valor1 = request.args.get(key="v1", default=None, type=float)
    valor2 = request.args.get(key="v2", default=None, type=float)
    if valor1 and valor2:
        return f" A soma do {valor1 + valor2}"
    return "Pensa Mark, Pensa Mark"
@app.route('/subtrair', methods=["GET"])
def subtrair():
    valor1 = request.args.get(key="v1", default=None, type=float)
    valor2 = request.args.get(key="v2", default=None, type=float)
    if valor1 and valor2:
     return f" A subtração do {valor1 - valor2}"
    return "Pensa Mark, Pensa Mark"
@app.route('/multiplicar', methods=["GET"])
def multiplicar():
    valor1 = request.args.get(key="v1", default=None, type=float)
    valor2 = request.args.get(key="v2", default=None, type=float)
    if valor1 and valor2:
     return f" A multiplicação do {valor1 * valor2}"
    return "Pensa Mark, Pensa Mark"

@app.route('/dividir',methods = ["GET"])
def dividir():
    valor1 = request.args.get(key="v1", default=None, type=float)
    valor2 = request.args.get(key="v2", default=None, type=float)
    if valor1 and valor2:
     return f" A divisao do {valor1 / valor2}"
    elif valor2 == 0:
        return f"Impossivel tal conta existir"
    return "Pensa Mark, Pensa Mark"



if __name__ == '__main__':

    app.run(debug=True)