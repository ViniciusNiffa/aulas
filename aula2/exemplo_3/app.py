from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home():
    n1 = 10
    n2 = 20
    total = n1 + n2

    # Formatação a saída da variável
    total_formatado = f"{total:.2f}"

    return render_template(
        "index.html",
        n1 = n1,
        n2 = n2,
        total = total,
        total_formatado = total_formatado

    )
if __name__ == "__main__":
    app.run(debug=True)