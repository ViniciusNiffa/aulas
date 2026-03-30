# Importa a classe Flask para criar aplicação web
from flask import Flask

# Importa função para renderizar HTML
from flask import render_template

# Importa objeto para manipular requisições
from flask import request

# Importa função para retornar JSON
from flask import jsonify

# Importa a classe Calculadora do arquivo calcular.py
from calculadora import Calculadora

# Cria a aplicação Flask
app = Flask(__name__)


# Define rota principal (página inicial)
@app.route("/", methods=["GET", "POST"])
def index():
    # Renderiza o arquivo index.html
    return render_template("index.html")


# Define rota que receberá dados via AJAX
@app.route("/calcular", methods=["POST"])
def calcular_ajax():

    # Recebe os dados enviados em formato JSON
    dados = request.get_json()

    # Obtém o primeiro valor enviado
    valor1 = dados.get("valor1")

    # Obtém o segundo valor enviado
    valor2 = dados.get("valor2")

    # Obtém a operação escolhida
    operacao = dados.get("operacao")

    # Cria objeto da classe Calculadora
    calc = Calculadora()

    # Define o primeiro valor
    calc.set_valor1(valor1)

    # Define o segundo valor
    calc.set_valor2(valor2)

    # Executa o cálculo conforme operação
    resultado = calc.calcular(operacao)

    # Retorna o resultado no formato JSON
    return jsonify({"resultado": resultado})


# Verifica se o arquivo está sendo executado diretamente
if __name__ == "__main__":
    # Inicia o servidor em modo debug
    app.run(debug=True)