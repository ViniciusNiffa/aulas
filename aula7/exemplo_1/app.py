from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

# Define a rota para o calculo usando o match-case
@app.route("/calculo_match", methods=["POST"])
def calculo_match():
    # Captura os valores enviados via POST
    num1=float(request.form.get("num1"))
    num2=float(request.form.get("num2"))
    operacao=str(request.form.get("operacao"))
    resultado=None
    
    # Estrutura do match-case
    match operacao:
        case "+":
            resultado=num1+num2
        case "-":
            resultado=num1-num2
        case "*":
            resultado=num1*num2
        case "/":
            if num2 !=0:
                resultado=num1/num2
            else:
                resultado= "Erro: divisão por zero"
        case _:
            resultado="Erro: Operação inválida"
        
    return render_template("resultado_match.html", resultado=resultado)

# Define a rota para cáluclar usando if/else
@app.route("/calculo_if", methods=["POST"])
def calculo_if():
    # Captura os valores enviados via POST
    num1=float(request.form.get("num1"))
    num2=float(request.form.get("num2"))
    operacao=str(request.form.get("operacao"))
    resultado=None
    
    if operacao== "+":
        resultado=num1+num2
    elif operacao=="-":
        resultado=num1-num2
    elif operacao=="*":
        resultado=num1*num2
    elif operacao=="/":
        if num2 !=0:
            resultado=num1/num2
        else:
            resultado="Erro: divisão por zero"
    else:
        "Erro: Operação inválida"
        
    return render_template("resultado_if.html",resultado=resultado)

if __name__=="__main__":
    app.run(debug=True)