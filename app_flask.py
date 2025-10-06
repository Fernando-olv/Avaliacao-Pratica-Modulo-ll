from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

## Continue o código aqui.
@app.route("/somar")
def soma():
    valor1 = request.args.get(key="valor1", default=None, type=float)
    valor2 = request.args.get(key="valor2", default=None, type=float)
    return f"A soma é{valor1+valor2}"

app.route("/subtrair")
def subtrair():
    valor1= float(request.args.get("Valor 1", 0))
    valor2= float(request.args.get("Valor 2", 0))
    return f"O resultado é{valor1-valor2}"

app.route("/multiplicar")
def multiplicar():
    valor1 = float(request.args.get ("Valor 1", 0))
    valor2= float(request.args.get("Valor 2", 0))
    return f"O resultado é{valor1*valor2}"

app.route("/dividir")
def dividir ():
    valor1 = float(request.args.get("valor1", 0))
    valor2 = float(request.args.get("valor2", 1))
    return f"O resultado é {valor1/valor2}"


if __name__ == "__main__":
    app.run(debug=True)
