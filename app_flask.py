from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/soma')
def soma():

    valor1 = request.args.get(key="valor1", default=0, type=float)
    valor2 = request.args.get("valor2", 0, float)
    return f"Soma = {valor1 + valor2}"

@app.route('/subtracao')
def subtracao():
    valor1 = request.args.get(key="valor1", default=0, type=float)
    valor2 = request.args.get("valor2", 0, float)
    return f"Subtração = {valor1 - valor2}"

@app.route('/divisao')
def divisao():
    valor1 = request.args.get(key="valor1", default=0, type=float)
    valor2 = request.args.get("valor2", 0, float)
    if valor2 == 0:
        return {"erro": "Divisão por zero não é permitida"}
    return f"Divisão = {valor1 // valor2}"


@app.route('/multiplicacao')
def multiplicacao():
    valor1 = request.args.get(key="valor1", default=0, type=float)
    valor2 = request.args.get("valor2", 0, float)
    return f"Multiplicação = {valor1 * valor2}"


if __name__ == "__main__":
    app.run(debug=True)
