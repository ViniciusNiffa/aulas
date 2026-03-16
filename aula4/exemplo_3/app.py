from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    array1 = [10,20,30,40,50]
    array2 = [11,12,13,14,15]

    # Array dinâmico
    a = []
    a.append(100)
    a.append(200)
    a.append(300)
    a.append(400)
    a.append(500)
    a.append("Teste") # String
    a.append(50.0) # Float
    a.append(True) # Booleano True
    a.append(False) # Booleano False

    b = {}
    b['a'] = 10
    b['b'] = 20
    b['c'] = 30
    b['d'] = 40
    b['e'] = "Letra e"
    b['letra e'] = 'Indice E'

    aluno = {}
    aluno["joao"] = {
        "idade": 20,
        "pai": "joaquim",
        "endereco": "Venâncio aires 93",
        "Nota": 5.5
    }
    aluno["abel"] = {
        "Idade": 23,
        "pai": "José",
        "endereco": "Venâncio aires 93",
        "Nota": 9.5
    }
    aluno["maria"] = {
        "Idade": 30,
        "pai": "Paulo",
        "endereco": "José do patrocínio 93",
        "Nota": 10
    }
    aluno["Paulo"] = {
        "Idade": 40,
        "pai": "Fábio",
        "endereco": "Venâncio Aires 93",
        "Nota": 5
    }

    a2 = [10,20,30,40,50,60,70,80,90]
    b2 = [1,2,3,4,5,6,7,8,9]

    c = []
    c.append(100)
    c.append(101)
    c.append(102)

    return render_template(
        "index.html",
        array1=array1,
        array2=array2,
        a=a,
        b=b,
        aluno=aluno,
        a2=a2,
        b2=b2,
        c=c
    )

if __name__ == "__main__":
    app.run(debug=True)