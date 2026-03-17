from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    i = 1
    resultados = []
    while i < 1000:
        valor_atual = i
        i *= 2
        resultados.append(f"{valor_atual} vezes 2 é igual a {i}")
    
    # Exemplo 2
    contador = 1
    contagem = []
    while contador <= 5:
        contagem.append(f"Número: {contador}")
        contador += 1
    
    # Exemplo3 - soma acumulativa
    numero = 1
    soma = 0
    soma_lista = []
    while numero <= 5:
        soma += numero
        soma_lista.append(f"Soma até {numero} = {soma}")
        numero += 1

    # Exemplo 4
    x = 1
    exemplo_break = []
    while True:
        exemplo_break.append(f"Valor atual: {x}")
        if x == 3:
            break
        x += 1

    return render_template(
        "index.html",
        resultados=resultados,
        contagem=contagem,
        soma_lista=soma_lista,
        exemplo_break=exemplo_break
    )
if __name__ == "__main__":
    app.run(debug=True)