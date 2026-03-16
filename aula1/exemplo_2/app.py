#importar a classe Flask da biblioteca Flask
from flask import Flask, render_template
# Cria a aplicação Flask
app = Flask(__name__)
# Define a rota principal do site
@app.route("/")
def home():
    # Variaveis no Python
    a = "Olá mundo !"
    b = "Meu código no Python :)"

    # Envia as variáveis para o HTML
    return render_template("index.html", a=a, b=b)

# Executa o servidor apenas se este arquivo for executado diretamente
if __name__ == "__main__":
    # debug=True ativa o modo desenvolvimento (atualiza automaticamente)
    app.run(debug=True)