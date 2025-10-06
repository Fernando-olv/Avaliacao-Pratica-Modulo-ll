from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

## Continue o código aqui.
@app.route('/soma')
def soma():
    valor1 = request.args.get(key="valor1", default= None, type=float)
    valor2 = request.args.get(key = "valor2", default= None, type=float)
    
    return f"Soma = {valor1 + valor2}"

@app.route('/subtrair')
def subtrair():
    valor_sub1 = request.args.get(key="valor_sub1", default= None, type=float)
    valor_sub2 = request.args.get(key = "valor_sub2", default= None, type=float)

    return f"Subtrair = {valor_sub1 - valor_sub2}"

@app.route('/multiplicacao')
def multiplicacao():
    valor_mult1 = request.args.get(key="valor_sub1", default= None, type=float)
    valor_mult2 = request.args.get(key="valor_sub1", default= None, type=float)
    
    return f"Multiplicacao = {valor_mult1 * valor_mult2}" 


if __name__ == "__main__":
    app.run(debug=True)
