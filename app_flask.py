from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

## Continue o código aqui.

@app.route("/soma")
def soma():
    valor1 = request.args.get(key="valor1", default=None, type=float)
    valor2 = request.args.get(key="valor2", default=None, type=float)
    return f"{valor1 + valor2}"

@app.route("/subtrair")
def subtrair():
    valor1 = request.args.get(key="valor1", default=None, type=float)
    valor2 = request.args.get(key="valor2", default=None, type=float)
    return f"{valor1 - valor2}"

@app.route("/multiplicar")
def multiplicar():
    valor1 = request.args.get(key="valor1", default=None, type=float)
    valor2 = request.args.get(key="valor2", default=None, type=float)
    return f"{valor1 * valor2}"

@app.route("/dividir")
def dividir():
    valor1 = request.args.get(key="valor1", default=None, type=float)
    valor2 = request.args.get(key="valor2", default=None, type=float)
    return f"{valor1 / valor2}"

if __name__ == "__main__":
    app.run(debug=True)
