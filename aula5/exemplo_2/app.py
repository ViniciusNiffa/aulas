from flask import Flask, render_template
# Importa datetime para trabalhar com data e hora
from datetime import datetime
# Importa ZoneInfo para definir o fuso horário
from zoneinfo import ZoneInfo

app = Flask(__name__)
@app.route("/")
def index():
    # Define o fuso horário de São Paulo
    fuso = ZoneInfo("America/Sao_Paulo")
    # Obtém data e hora atual com fuso configurado
    agora = datetime.now(fuso)

    #weekday() retorna:
    #0 = domingo...6 = sábado
    wday = (agora.weekday() + 1) % 7

    match wday:
        case 0:
            mensagem = "Domingo sonolento"
        case 1:
            mensagem = "Segunda é dia da aula do meu querido professor Miguel"
        case 2:
            mensagem = "Terça é dia de desafio no Senac"
        case 3:
            mensagem = "Quarta é dia de jogar um game"
        case 5:
            mensagem = "Uhuuul, sextou"
        case 6:
            mensagem = "Sábado é dia de jogar até a madrugada"
        case _:
            mensagem = "Quinta é dia do PIDS Tech do sor Miguel"

    return render_template(
        "index.html",
        mensagem=mensagem
    )
if __name__ == "__main__":
    app.run(debug=True)