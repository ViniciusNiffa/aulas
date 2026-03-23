from flask import Flask, render_template, request
app = Flask(__name__)

# Função para definir a alíquota do INSS
def buscar_liquota_inss(salario_bruto):
    if salario_bruto <= 1412.00:
        return 7.5
    elif salario_bruto <= 266.68:
        return 9
    elif salario_bruto <= 4000.03:
        return 12
    elif salario_bruto <= 7786.02:
        return 14
    else:
        return 14 # Teto
    
# Rota principal
@app.route("/")
def index():
    return render_template("index.html")

# Rota de cálculo
@app.route("/calcular", methods=["POST"])
def calcular():
    valor_hora = float(request.form["valor_hora"])
    horas_trabalhadas = float(request.form["horas_trabalhadas"])
    salario_bruto = valor_hora * horas_trabalhadas
    vale_alimentacao = float(request.form["vale_alimentacao"])
    vale_transporte = float(request.form["vale_transporte"])
    # Cálculo INSS
    aliquota = buscar_liquota_inss(salario_bruto)
    desconto_inss = salario_bruto * (aliquota / 100)
    # Vale alimentação - desconto de 6% sobre o valor recebido
    desconto_va = vale_alimentacao * 0.06
    # Vale transporte - desconto de 6% sobre o salário bruto,
    # limitado ao valor recebido
    desconto_vt_calculado = salario_bruto * 0.06
    desconto_vt = min(desconto_vt_calculado, vale_transporte)

    # Total de descontos
    total_descontos = desconto_inss + desconto_va + desconto_vt
    # Salário liquido
    salario_liquido = salario_bruto - total_descontos
    return render_template(
        "resultado.html",
        valor_hora=valor_hora,
        horas_trabalhadas=horas_trabalhadas,
        salario_bruto=salario_bruto,
        aliquota=aliquota,
        desconto_inss=desconto_inss,
        desconto_va=desconto_va,
        desconto_vt=desconto_vt,
        salario_liquido=salario_liquido
    )
if __name__ == "__main__":
    app.run(debug=True)