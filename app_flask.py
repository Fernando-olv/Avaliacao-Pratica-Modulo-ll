from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

## Continue o código aqui.

@app.route('/soma')
def soma():
        valor1= request.args.get('valor1',default= 0, type=float)
        valor2= request.args.get('valor2',default= 0, type=float)
        return f'soma = {valor1 + valor2}'


@app.route('/subtrair')
def subtrair():
        valor1= request.args.get('valor1',default= 0, type=float)
        valor2= request.args.get('valor2',default= 0, type=float)
        return f'subtrair = {valor1 + valor2}'

@app.route('/multiplicar')
def multiplicar():
        valor1= request.args.get('valor1',default= 0, type=float)
        valor2= request.args.get('valor2',default= 0, type=float)
        return f'multiplicar = {valor1 + valor2}'

@app.route ('/dividir')
def dividir():
        valor1= request.args.get('valor1',default= 1, type=float)
        valor2= request.args.get('valor2',default= 1, type=float)
        return f'dividir = {valor1 + valor2}'


if __name__ == "__main__":
    app.run(debug=True)
