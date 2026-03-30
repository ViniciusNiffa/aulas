from flask import Flask, render_template, request
from funcionario import Funcionario
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/resultado", methods=["POST"])
def resultado():
    nome = request.form.get("nome")
    valor = request.form.get("valor")

    funcionario = Funcionario()

    funcionario.set_nome(nome)
    funcionario.set_valor_salario(valor)

    salario_liquido = funcionario.calcular()

    return render_template(
        "resultado.html",
        nome=funcionario.get_nome(),
        salario=salario_liquido
    )
if __name__ == "__main__":
    app.run(debug=True)