from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

## Continue o código aqui.

@app.route('/soma', methods=["GET"])
def soma ():
    valor1 = request.args.get(key="v1", default=None, type=float)
    valor2 = request.args.get(key="v2", default=None, type=float)
    if valor1 and valor2:
        return f"soma = {valor1 + valor2}"
    return "Não foi recebido v1 e v2 na ULR"

@app.route('/subtrair', methods=["GET"])
def subtrair():
    valor1 = request.args.get(key="v1", default=None, type=float)
    valor2 = request.args.get(key="v2", default=None, type=float)
    if valor1 and valor2:
        return f"subtrair = {valor1 - valor2}"
    return "Não foi recebido v1 e v2 na ULR"

        
@app.route('/multiplicaçao', methods=["GET"])
def multiplicaçao():
    valor1 = request.args.get(key="v1", default=None, type=float)
    valor2 = request.args.get(key="v2", default=None, type=float)
    if valor1 and valor2:
        return f"multiplicaçao = {valor1*valor2}"
    return "Não foi recebido v1 e v2 na ULR"

@app.route('/divisao', methods=["GET"])
def divisao():
    valor1 = request.args.get(key="v1", default=None, type=float)
    valor2 = request.args.get(key="v2", default=None, type=float)
    if valor1 and valor2:
        return f"divisao = {valor1 - valor2}"
    if valor2 == 0:
        return {"erro": "Divisão por zero não é permitida"}
    
    return "Não foi recebido v1 e v2 na ULR"


if __name__ == "__main__":
    app.run(debug=True)
