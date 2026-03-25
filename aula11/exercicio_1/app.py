from flask import Flask, render_template, request
app = Flask(__name__)

class Pessoa:
    def __init__(self):
        self._nome = None
        self._idade = None
        self._cpf = None
        self._email = None
        self._telefone = None
        self._endereco = None
        self._cidade = None
        self._estado = None
    
    def get_nome(self):
        return self._nome
    def get_idade(self):
        return self._idade
    def get_cpf(self):
        return self._cpf
    def get_email(self):
        return self._email
    def get_telefone(self):
        return self._telefone
    def get_endereco(self):
        return self._endereco
    def get_cidade(self):
        return self._cidade
    def get_estado(self):
        return self._estado
    
    def set_nome(self, nome):
        self._nome = nome
    def set_idade(self, idade):
        self._idade = idade
    def set_cpf(self, cpf):
        self._cpf = cpf
    def set_email(self, email):
        self._email = email
    def set_telefone(self, telefone):
        self._telefone = telefone
    def set_endereco(self, endereco):
        self._endereco = endereco
    def set_cidade(self, cidade):
        self._cidade = cidade
    def set_estado(self, estado):
        self._estado = estado
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/dados", methods=["POST"])
def dados():
    nome = request.form ["nome"]
    idade = request.form ["idade"]
    cpf = request.form ["cpf"]
    email = request.form ["email"]
    telefone = request.form ["telefone"]
    endereco = request.form ["endereco"]
    cidade = request.form ["cidade"]
    estado = request.form ["estado"]

    pessoa = Pessoa()

    pessoa.set_nome(nome)
    pessoa.set_idade(idade)
    pessoa.set_cpf(cpf)
    pessoa.set_email(email)
    pessoa.set_telefone(telefone)
    pessoa.set_endereco(endereco)
    pessoa.set_cidade(cidade)
    pessoa.set_estado(estado)

    return render_template(
        "resultados.html",
        nome=pessoa.get_nome(),
        idade=pessoa.get_idade(),
        cpf=pessoa.get_cpf(),
        email=pessoa.get_email(),
        telefone=pessoa.get_telefone(),
        endereco=pessoa.get_endereco(),
        cidade=pessoa.get_cidade(),
        estado=pessoa.get_estado()
    )
if __name__ == "__main__":
    app.run(debug=True)