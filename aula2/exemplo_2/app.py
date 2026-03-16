# Importa a classe Flask para criar a aplicação web
from flask import Flask, render_template
# Cria a aplicação Flask
app = Flask(__name__)
# Define a rota principal do site
@app.route("/")
def home():
    s = "Teste de impressão utilizando variável"
    n = 15
    d = 10.10
    t = "Exemplo de texto 22222222"
    b = True
    f = False

    # Variáveis com formatação
    decimal_normal = f"{n:d}" # Decimal simples
    decimal_8 = f"{n:8d}"     # 8 espaçoes
    decimal_08 = f"{n:08d}"   # 8 digitos com zero
    decimal_float = f"{n:.2f}" #2 casas decimais

    # Mostrando o tipo da variavel e valor
    tipos = {
        "t": f"{t} (tipo: {type(t).__name__})",
        "n": f"{n} (tipo: {type(n).__name__})",
        "d": f"{d} (tipo: {type(d).__name__})",
        "b": f"{b} (tipo: {type(b).__name__})",
        "f": f"{f} (tipo: {type(f).__name__})"

    }
    # Envia todas as variáveis para o HTML
    return render_template(
        "index.html",
        s=s,
        n=n,
        d=d,
        t=t,
        b=b,
        f=f,
        decimal_normal = decimal_normal,
        decimal_8 = decimal_8,
        decimal_08 = decimal_08,
        decimal_float = decimal_float,
        tipos = tipos
    )
# Executa o servidor
if __name__ == "__main__":
    app.run(debug=True)