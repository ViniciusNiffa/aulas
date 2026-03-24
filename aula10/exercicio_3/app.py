from flask import Flask, render_template, request
app = Flask(__name__)
# Rota principal
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

# Rota do processamento dos dados
@app.route("/calcular", methods=["POST"])
def calcular():
    nome = request.form["nome"]
    turma = request.form["turma"]
    notas = []
    notas.append(float(request.form["nota1"]))
    notas.append(float(request.form["nota2"]))
    notas.append(float(request.form["nota3"]))
    notas.append(float(request.form["nota4"]))
    notas.append(float(request.form["nota5"]))

    media = sum(notas) / len(notas)

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    
    return render_template(
        "resultado.html",
        nome=nome,
        turma=turma,
        notas=notas,
        media=media,
        situacao=situacao
    )
if __name__ == "__main__":
    app.run(debug=True)