# Define a classe funcionário
class Funcionario:
    # Método construtor (executa quando criamos o objeto)
    def __init__(self):
        self.__nome = ""
        self.__valorSalario = 0.0

    # Método GET para retornar os dados
    def get_nome(self):
        return self.__nome
    
    def get_valor_salario(self):
        return self.__valorSalario
    
    # Método SET para definir os dados
    def set_nome(self, nome):
        self.__nome = nome

    def set_valor_salario(self, valor):
        self.__valorSalario = float(valor)

    # Método para calcular o salário líquido
    def calcular(self):
        calc = 0

        if 0 < self.__valorSalario <= 900:
            # Não há desconto
            calc = self.__valorSalario
        elif 900 < self.__valorSalario <= 1800:
            calc = self.__valorSalario -(self.__valorSalario * 0.15)
        elif self.__valorSalario > 1800:
            calc = self.__valorSalario - (self.__valorSalario * 0.27)

        return f"{calc:,.2f}"                

    