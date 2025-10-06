from flask import Flask, request
app = Flask (__name__)

@app.route('/')
def olá():
    return "olá, Flask!"

@app.route('/soma', methods=["GET"])
def soma ():
    valor1 = request.args.get(key= "valor1", default=None, type=float)
    valor2 = request.args.get(key = "valor2", default=None,type=float)

    return f"Soma = {valor1 + valor2}"

@app.route('/subtrair', methods=["GET"])
def subtrair():
    valor1 = request.args.get(key= "valor1", default=None, type=float)
    valor2 = request.args.get(key = "valor2", default=None,type=float)

    return f"subtrair = {valor1 - valor2}"

@app.route('/multiplicacao', methods=["GET"])
def multiplicacao():
    valor1 = request.args.get(key= "valor1", default=None, type=float)
    valor2 = request.args.get(key = "valor2", default=None,type=float)

    return f"multiplicacao = {valor1 * valor2}"

@app.route('/divisao', methods=["GET"])
def divisao():
    valor1 = request.args.get(key= "valor1", default=None, type=float)
    valor2 = request.args.get(key = "valor2", default=None,type=float)

    return f"divisao = {valor1 / valor2}"

   
if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
