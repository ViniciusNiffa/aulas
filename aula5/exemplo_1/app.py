from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    x = 0
    if x > 10:
        msg1 = "O valor da variável é maior que 10"
    else:
        msg1 = "O valor da variável é igual a 10 ou menor"

    # Utilizando operadores lógicos
    if (x > 10) and (x <= 10):
        msg2 = "O valor da variável é entre 0 e 10"
    else:
        msg2 = "O valor da variável não é entre 0 e 10"
    
    if (x == 0) or (x == 10):
        msg3 = "O valor da variável é 0 ou 10"
    else:
        msg3 = "O valor da variável não é zero ou 10"
    
    return render_template(
        "index.html",
        msg1=msg1,
        msg2=msg2,
        msg3=msg3
    )
if __name__ == "__main__":
    app.run(debug=True)