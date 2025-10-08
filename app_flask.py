from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/soma")
def soma():
    valor1 = request.args.get("valor1", type=float)
    valor2 = request.args.get("valor2", type=float)

    return f"Soma = {valor1 + valor2}"

@app.route("/subtrair")
def subtrair():
    valor1 = request.args.get("valor1", type=float)
    valor2 = request.args.get("valor2", type=float)

    return f"Subtrair = {valor1 - valor2}"


@app.route("/dividir")
def dividir():
    valor1 = request.args.get("valor1", type=float)
    valor2 = request.args.get("valor2", type=float)
    if valor2 == 0:
        return "Impossível dividir por zero."
    return f"Dividir = {valor1 / valor2}"

@app.route("/multiplicar")
def multiplicar():
    valor1 = request.args.get("valor1", type=float)
    valor2 = request.args.get("valor2", type=float)

    return f"Multiplicar = {valor1 * valor2}"





if __name__ == "__main__":
    app.run(debug=True)
