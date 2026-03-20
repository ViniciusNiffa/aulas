from flask import Flask,render_template, request
app= Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

# Define a rota que recebe os dados via POST

@app.route("/parouimpar", methods=["POST"])
def parouimpar():
    numero=int(request.form.get("numero"))
    
    # Criar uma lista vazia para armazenar os resultados
    resultados=[]
    
    # Loop que vai ter 1 at´w o número informado no formulario
    for n in range(1, numero+1):
        # Verifica se o número é par ou impar
        if n % 2==0:
            # Adiciona um dicionário com o número, tipo
            resultados.append({
                "numero": n,
                "tipo": "Par",
                "cor": "red"
            })
        else:
            resultados.append({
                "numero": n,
                "tipo": "Ímpar",
                "cor": "yellow"
            })
    
    # Envia a lista de resultado para o template resultado.html
    return render_template("resultado.html",resultados=resultados)

if __name__=="__main__":
    app.run(debug=True)