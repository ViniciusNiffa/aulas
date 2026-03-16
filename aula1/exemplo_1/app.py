# Importar a classe Flask da biblioteca flask
from flask import Flask

# Importar o módulo sys para pegar a versão do python
import sys


# Criar a aplicação Flask
app = Flask(__name__)

# Definir a rota principal do site
@app.route("/")
def home():
    # Retorna o HTML como reposta
    return f""" 
    <!DOCTYPE html>
    <html lang="pt-br">
        <head>
            <title>Meu primeiro site de Python Web</title>
            <meta charset="utf=8">
        </head>
        <body>
            <p>Alo mundo utilizando HTML e Python</p>
            <p>Python version: {sys.version}</p>
            <p>Que emoção!</p>
        </body
    </html>
"""
#Executa o servidor quando rodar o arquivo
if __name__ == "__main__":
    app.run(debug=True)