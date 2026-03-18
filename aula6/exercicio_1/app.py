from flask import Flask, render_template

from flask import request

app = Flask (__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/meusDados")
def dados():
    nome = request.args.get("nome")
    nasc = request.args.get("nasc")
    idade = request.args.get("idade")
    endereco = request.args.get("endereco")
    bairro = request.args.get("bairro")
    cidade = request.args.get("cidade")
    estado = request.args.get("estado")
    celular = request.args.get("celular")
    email = request.args.get("email")
    cpf = request.args.get("cpf")
    rg = request.args.get("rg")
    
    if nome and nasc and idade and endereco and bairro and cidade and estado and celular and email and cpf and rg:
        mensagem = "Dados cadastrados com sucesso!"
    else:
        mensagem = "Nenhum dado foi cadastrado"
    
    return render_template(
        "meusDados.html",
        nome=nome,
        nasc=nasc,
        idade=idade,
        endereco=endereco,
        bairro=bairro,
        cidade=cidade,
        estado=estado,
        celular=celular,
        email=email,
        cpf=cpf,
        rg=rg,
        mensagem=mensagem
    )
if __name__ == "__main__":
    app.run(debug=True)