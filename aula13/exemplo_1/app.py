from flask import Flask, render_template, request 
from funcionario import Funcionario
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/resultado", methods=["POST"])
def resultado():
    funcionario = Funcionario()
    funcionario.set_nome(request.form.get("nome"))
    funcionario.set_salario_bruto(request.form.get("salario"))
    funcionario.set_vale_alimentacao(request.form.get("vale_alimentacao"))
    funcionario.set_vale_transporte(request.form.get("vale_transporte"))

    liquido = funcionario.calcular_salario_liquido()

    return render_template(
        "resultado.html",
        nome=funcionario.get_nome(),
        bruto=f"{funcionario.get_salario_bruto():,.2f}",
        inss=f"{funcionario.get_inss():,.2f}",
        ir=f"{funcionario.get_ir():,.2f}",
        desconto_va=f"{funcionario.get_desconto_va():,.2f}",
        desconto_vt=f"{funcionario.get_desconto_vt():,.2f}",
        liquido=f"{liquido:,.2f}"
    )
if __name__ == "__main__":
    app.run(debug=True)