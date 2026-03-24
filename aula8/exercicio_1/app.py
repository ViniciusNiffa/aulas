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
        juros_percentual = 0.05
    elif 4 <= atraso <= 9:
        juros_percentual = 0.10
    elif atraso >= 10:
        juros_percentual = 0.15
    elif atraso < 0:
        return "Digite valores válidos!"
    else:
        juros_percentual = 0
    
    if prestacao < 0:
        return "Digite valores válidos!"
    
    juros = prestacao * juros_percentual
    total = juros + prestacao

    return render_template(
        "calcJu.html",
        prestacao = prestacao,
        atraso = atraso,
        juros = juros,
        total = total
        )

if __name__ == "__main__":
    app.run(debug=True)