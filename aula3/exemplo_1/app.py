from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    # Trabalhando com funções

    # Define uma função que retorna uma mensagem
    def msg():
        return "Hello world!"
    
    # Chama a função
    mensagem = msg()

    # Função que recebe um nome
    def nomeAluno(aluno):
        return aluno
    
    # Lista de alunos (chamada pela função)
    alunos = [
        nomeAluno("Miguel"),
        nomeAluno("Clotilde"),
        nomeAluno("Juvenildo"),
        nomeAluno("Valdisney"),
        nomeAluno("Jevenino"),
    ]

    # Função que recebe dois argumentos, nome e idade
    def nomeIdade(nome, idade):
        return f"Seu nome é: {nome}, e sua idade é: {idade}"
    
    # Lista com o nome e idade
    pessoas = [
        nomeIdade("Juvenildo", 20),
        nomeIdade("Valdisney", 21),
        nomeIdade("Jevenino", 22)
    ]
    # Declaração de variável do tipo global
    global b
    # Função para somar
    def soma(a):
        global b
        b = a + 5

    # Chama a função
    soma(10)

    valor_b = b
     
    # Outro exemplo de variável global
    global a
    a = 1
    b = 2

    def calcula():
        global a, b
        b = a + b
    
    calcula()
    resultado_calculo = b

    # Envia todos os dados para o HTML
    return render_template(
        "index.html",
        mensagem=mensagem,
        alunos=alunos,
        pessoas=pessoas,
        valor_b=valor_b,
        resultado_calculo=resultado_calculo
    )
# Executa o servidor
if __name__ == "__main__":
    app.run(debug=True)

