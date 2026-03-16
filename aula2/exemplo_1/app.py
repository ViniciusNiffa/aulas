# Importar a classe do Flask
from flask import Flask, render_template
# Cria a aplicação Flask
app = Flask(__name__)
# Define a rota principal
@app.route("/")
def home():
    # Variáveis Python
    nome = "Valdisney"
    idade = 22
    endereco = "Venâncio Aires 93"
    bairro = "CB"

    # Envia as variáveis para o HTML
    return render_template(
        "index.html",
        nome=nome,
        idade=idade,
        endereco=endereco,
        bairro=bairro
    )
# Executa o servidor
if __name__ == "__main__":
    app.run(debug=True)