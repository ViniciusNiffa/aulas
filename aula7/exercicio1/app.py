from flask import Flask, render_template,request
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculo_media", methods=["POST"])
def calculo_media():
    nome=str(request.form.get("nome"))
    turma=float(request.form.get("turma"))
    n1=int(request.form.get("n1"))
    n2=int(request.form.get("n2"))
    n3=int(request.form.get("n3"))
    n4=int(request.form.get("n4"))

    media_final= (n1+n2+n3+n4)/4
    situacao=None
    
    if media_final>=7:
        situacao= "Aprovado"
    elif media_final>=5:
        situacao= "Recuperacao"
    elif media_final<5:
        situacao= "Reprovado"
    else:
        situacao="Dgite valores válidos"
    
    return render_template("situacao.html",situacao=situacao,nome=nome,turma=turma,media_final=media_final,n1=n1,n2=n2,n3=n3,n4=n4)

if __name__=="__main__":
    app.run(debug=True)