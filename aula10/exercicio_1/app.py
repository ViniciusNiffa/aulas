from flask import Flask, render_template, request
app = Flask(__name__)

# Rota principal
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

# Rota que recebe os dados
@app.route("/processar", methods=["POST"])
def processar():
    n1 = request.form["n1"]
    n2 = request.form["n2"]
    n3 = request.form["n3"]

    # Criar uma lista vazia
    nomes = []

    # Adicionar os valores recebidos na lista
    nomes.append(n1)
    nomes.append(n2)
    nomes.append(n3)

    return render_template("resultado.html", nomes=nomes)
if __name__ == "__main__":
    app.run(debug=True)