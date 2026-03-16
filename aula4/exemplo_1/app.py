from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    # Sistema para calcular notas
    # Criando uma função para calcular a média
    global media
    # Define a função que recebe 4 notas
    def soma(n1, n2, n3, n4):
        global media
        media = (n1+n2+n3+n4) / 4
    
    soma(9, 8, 7, 6)

    media_normal = media

    media_formatada = f"{media:.2f}"

    return render_template(
        "index.html",
        media_normal=media_normal,
        media_formatada=media_formatada
    )
if __name__=="__main__":
    app.run(debug=True)