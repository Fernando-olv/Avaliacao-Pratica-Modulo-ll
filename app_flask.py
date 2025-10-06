from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

## Continue o código aqui.
@app.route('/soma')
def soma():
    valor1 = request.args.get(key="valor1", default=None ,type=float)
    valor2 = request.args.get (key="valor2" , default=None , type=float)
    return f"A soma é: {valor1 + valor2}"
@app.route('/subtrair')
def subtrair():
    valor3 =request.args.get(key='valor3', default=None, type= float)
    valor4 =request.args.get(valor4,0,float)
    return f"A soma é: {valor3 - valor4}"

if __name__ == "__main__":
    app.run(debug=True)