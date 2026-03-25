from flask import Flask, render_template, request
app = Flask(__name__)

# Criando a classe
class Aluno:
    # Método construtor da classe
    def __init__(self):
        # Atribuidos privados
        self._nome = None
        self._idade = None

    # Método GET para retornar valores
    def get_nome(self):
        return self._nome
    
    def get_idade(self):
        return self._idade
    
    # Metódo SET alteram os valores
    def set_nome(self, nome):
        self._nome = nome
    
    def set_idade(self, idade):
        self._idade = idade

# Rota principal
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

# Rota de processamento dos dados
@app.route("/dados", methods=["POST"])
def dados():
    # Recebe os dados enviados pelo formulário
    nome = request.form ["nome"]
    idade = request.form["idade"]
    
    # Cria uma instância do objeto da classe Aluno
    aluno = Aluno()
    # Usa o método SET para inserir os dados
    aluno.set_nome(nome)
    aluno.set_idade(idade)

    return render_template(
        "resultado.html",
        nome=aluno.get_nome(),
        idade=aluno.get_idade()
    )
if __name__ == "__main__":
    app.run(debug=True)