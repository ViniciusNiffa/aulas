from flask import Flask, render_template, request
app = Flask(__name__)

# Função para calcular a folha de pagamento
def calcular_folha(valor_hora, horas_trabalhadas, desconto_percentual):
    # Calcula salário bruto
    salario_bruto = valor_hora * horas_trabalhadas
    # Calcula valor do desconto
    valor_desconto = salario_bruto * (desconto_percentual / 100)
    # Calculo salário liquido
    salario_liquido = salario_bruto - valor_desconto
    # Retorna todos os valores calculados
    return salario_bruto, valor_desconto, salario_liquido

# Rota principal
@app.route("/")
def formulario():
    return render_template("index.html")

# Rota que processa os dados
@app.route("/calcular", methods=["POST"])
def calcular():
    try:
        # Recebe os valores e converte para float
        valor_hora = float(request.form["valorHora"])
        horas_trabalhadas = float(request.form["horasTrabalhadas"])
        desconto = float(request.form["desconto"])

        if valor_hora <= 0 or horas_trabalhadas <= 0 or desconto < 0:
            erro = "Valores inválidos! Verifique os dados digitados."
            return render_template("index.html", erro=erro)
        
        # Chama a função de cálculo
        salario_bruto, valor_desconto, salario_liquido = calcular_folha(
            valor_hora,
            horas_trabalhadas,
            desconto
        )
        # Envia os dados para a página de resultado
        return render_template(
            "resultado.html",
            valor_hora=valor_hora,
            horas_trabalhadas=horas_trabalhadas,
            desconto=desconto,
            salario_bruto=salario_bruto,
            valor_desconto=valor_desconto,
            salario_liquido=salario_liquido
        )
    except ValueError:
        # Caso ocorra erro de conversão
        erro = "Erro a processar os dados. Digite valores válidos"
        return render_template("index.html", erro=erro)
if __name__ == "__main__":
    app.run(debug=True)