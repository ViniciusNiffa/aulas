# Instalar a biblioteca para PDF:
# pip install reportlab

from flask import Flask, render_template, request, send_file
# Importar a classe funcionário
from funcionario import Funcionario
# Importar a biblioteca PDF
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Recebe dados do formulário
        nome = request.form.get("nome")
        valor_hora = request.form.get("valor_hora")
        horas = request.form.get("horas")
        vale_alimentacao = request.form.get("vale_alimentacao")
        vale_transporte = request.form.get("vale_transporte")

        # Cria objeto funcionario
        funcionario = Funcionario(
            nome,
            valor_hora,
            horas,
            vale_alimentacao,
            vale_transporte
        )
        # Gera o PDF automaticamente
        gerar_pdf(funcionario)

        return render_template("resultado.html", f=funcionario)
    return render_template("index.html")
# Função para gerar o PDF
def gerar_pdf(funcionario):
    # Define o nome do arquivo
    arquivo = f"{funcionario.nome}_folha.pdf"
    # Cria documento PDF
    doc = SimpleDocTemplate(arquivo, pagesize=A4)
    
    elementos = []
    #Lisa de alimentos do PDF
    estilos = getSampleStyleSheet()

    elementos.append(Paragraph("Relatório de folha de pagamento", estilos["Title"]))
    elementos.append(Spacer(1, 12))
    elementos.append(Paragraph(f"Nome: {funcionario.nome}", estilos["Normal"]))
    elementos.append(Paragraph(f"Salário bruto: {funcionario.salario_bruto:.2f}", estilos["Normal"]))
    elementos.append(Paragraph(f"INSS: {funcionario.inss:.2f}", estilos["Normal"]))
    elementos.append(Paragraph(f"IRRF: {funcionario.irrf:.2f}", estilos["Normal"]))
    elementos.append(Paragraph(f"Desconto VA: {funcionario.desconto_va:.2f}", estilos["Normal"]))
    elementos.append(Paragraph(f"Desconto VT: {funcionario.desconto_vt:.2f}", estilos["Normal"]))
    elementos.append(Paragraph(f"Salário líquido: {funcionario.salario_liquido:.2f}", estilos["Normal"]))

    # Gerar arquivo
    doc.build(elementos)

if __name__ == "__main__":
    app.run(debug=True)