from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculo_juros", methods=["POST"])

def calculo_juros():
    prestacao = float(request.form.get("prestacao"))
    atraso = int(request.form.get("atraso"))
    
    if 1 <= atraso <= 3:
        juros = 0.05
    elif 4 <= atraso <= 9:
        juros = 0.10
    elif atraso >= 10:
        juros = 0.15
    else:
        juros = "Digite valores válidos"
    
    total = prestacao * juros

    return render_template(
        "calcJu.html",
        prestacao = prestacao,
        atraso = atraso,
        juros = juros,
        total = total
        )

if __name__ == "__main__":
    app.run(debug=True)