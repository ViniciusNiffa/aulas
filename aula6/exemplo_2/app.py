from flask import Flask
from flask import render_template

# Importa o request para capturar os dados enviados pelo formulário
from flask import request

app = Flask (__name__)
@app.route("/")
def index():
    # Renderiza o arquivo index.html
    return render_template("index.html")
# Processamento dos dados
# Define a rota /dados (GET é padrão no Flask)
@app.route("/dados")
def dados():
    # Captura o valor enviado pelo campo "nome"

    nome = request.args.get("nome")
        # Captura o valor enviado pelo campo "idade"
    idade = request.args.get("idade")
    # Verificar se os dados foram enviados
    if nome and idade:
        mensagem = "Dados cadastrados com sucesso!"
    else:
        mensagem = "Nenhum dado foi enviado."
    
    # Envia os dados para o template dados.html
    return render_template(
        "dados.html",
        nome=nome, 
        idade=idade,
        mensagem=mensagem
        )

if __name__ == "__main__":
    app.run(debug=True)