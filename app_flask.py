from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

## Continue o código aqui.

@app.route('/soma',methods= ["GET"])
def soma ():
    valor1 = request.args.get(key= "v1",default = None,type = float)
    valor2 = request.args.get (key= "v2",default = None ,type=float)
    return f"soma= {valor1 + valor2}"

@app.route("/subtrair",methods= ["GET"])
def subtrair():
    valor1 = request.args.get(key= "v1",default = None,type = float)
    valor2 = request.args.get (key= "v2",default = None ,type=float)
    return f"subtrair= {valor1 - valor2}"

@app.route("/dividir",methods= ["GET"])
def dividir():
    valor1 = request.args.get(key= "v1",default = None,type = float)
    valor2 = request.args.get (key= "v2",default = None ,type=float)
    return f"dividir= {valor1 / valor2}"

@app.route("/multiplicar",methods= ["GET"])
def multiplicar():
    valor1 = request.args.get(key= "v1",default = None,type = float)
    valor2 = request.args.get (key= "v2",default = None ,type=float)
    return f"multiplicar= {valor1 * valor2}"

if __name__ == "__main__":
    app.run(debug=True)