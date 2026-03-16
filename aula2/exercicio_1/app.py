from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home():
    n1 = 5
    n2 = 3
    n3 = 2
    n4 = 10
    situacao = ""
    total = (n1 + n2 + n3 + n4) / 4
    if total <= 10 :
        situacao = "Aprovado"
    elif total <= 6 :
        situacao = "Recuperação"
    elif total <= 4 :
        situacao = "Burrooo"
    else:
        situacao = "Uma anemona teria uma nota melhor que a sua"

    total_formatado = f"{total:.2f}"
    return render_template(
        "index.html",
        n1=n1,
        n2=n2,
        n3=3,
        n4=n4,
        total=total,
        total_formatado=total_formatado,
        situacao=situacao
        )
if __name__=="__main__":
    app.run(debug=True)