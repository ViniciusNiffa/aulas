from flask import Flask, render_template, request
from pessoa import Pessoa
app = Flask(__name__)

# Rota principal
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

# Rota de processamento dos dados
@app.route("/resultado", methods=["POST"])
def resultado():
    # Recebe os dados enviados pelo formulário
    nome = request.form["nome"]
    idade = request.form["idade"]
    cpf = request.form["cpf"]
    email = request.form["email"]
    telefone = request.form["telefone"]
    endereco = request.form["endereco"]
    cidade = request.form["cidade"]
    estado = request.form["estado"]

    pessoa = Pessoa(nome,idade,cpf,email,telefone,endereco,cidade,estado)

    return render_template(
        "resultado.html",
        dados = pessoa.dados_formatados()
    )
if __name__ == "__main__":
    app.run(debug=True)

