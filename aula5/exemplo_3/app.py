from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    # Criar uma lista vazia para armazenar as linhas
    linhas = []
    for i in range (1, 10):
        #Adiciona cada linha na lista
        linhas.append(f"Linha {i}")

    # Contagem regressiva
    regressiva = []
    for i in range(5, 0, -1):
        regressiva.append(f"Contagem: {i}")

    # Percorrendo a lista
    nomes = ["Juvenino", "Clotilde", "Valdisney", "Clementino"]
    lista_nomes = []
    for nome in nomes:
        lista_nomes.append(f"Nome: {nome}")
    
    # Tabuada simples
    numero = 3
    tabuada = []
    for i in range(1, 11):
        resultado = numero * i
        tabuada.append(f"{numero} x {i} = {resultado}")
    
    return render_template(
        "index.html",
        linhas=linhas,
        regressiva=regressiva,
        lista_nomes=lista_nomes,
        tabuada=tabuada
    )
if __name__ == "__main__":
    app.run(debug=True)