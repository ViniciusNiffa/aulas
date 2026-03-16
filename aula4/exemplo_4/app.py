from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    # Trabalhando com a função if else
    x = 20
    if x > 10:
        mensagem = "O valor da variável é menor que 10"
    else:
        mensagem = "O valor da variável ou é igual a 10 ou menor"

    return render_template(
        "index.html",
        mensagem=mensagem
    )
if __name__ == "__main__":
    app.run(debug=True)