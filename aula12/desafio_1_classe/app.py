# Importa a classe Flask
from flask import Flask, render_template, request

# Importa a classe Calcular do arquivo calcular.py
from calcular import Calcular

# Cria a aplicação Flask
app = Flask(__name__)


# Define a rota principal (abre o formulário)
@app.route("/", methods=["GET", "POST"])
def index():
    # Renderiza o arquivo index.html
    return render_template("index.html")


# Define a rota que receberá os dados do formulário
@app.route("/resultado", methods=["POST"])
def resultado():

    # Recebe o primeiro valor digitado
    valor1 = request.form.get("valor1")

    # Recebe o segundo valor digitado
    valor2 = request.form.get("valor2")

    # Recebe a operação digitada (+ - * /)
    operacao = request.form.get("operacao")

    # Instancia a classe Calcular
    calc = Calcular()

    # Define o valor1 usando método SET
    calc.set_valor1(valor1)

    # Define o valor2 usando método SET
    calc.set_valor2(valor2)

    # Estrutura condicional equivalente ao switch do PHP
    if operacao == "+":
        resultado = calc.soma()

    elif operacao == "-":
        resultado = calc.subtracao()

    elif operacao == "*":
        resultado = calc.multi()

    elif operacao == "/":
        resultado = calc.div()

    else:
        resultado = "Operação inválida"

    # Envia o resultado para o template HTML
    return render_template("resultado.html", resultado=resultado)


# Executa o servidor Flask
if __name__ == "__main__":
    # Ativa modo debug
    app.run(debug=True)