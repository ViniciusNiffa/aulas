# Define a classe Calculadora
class Calculadora:

    # Método construtor da classe (executa ao criar o objeto)
    def __init__(self):
        # Atributo privado que armazena o primeiro valor
        self.__valor1 = 0.0
        # Atributo privado que armazena o segundo valor
        self.__valor2 = 0.0

    # Método para definir o primeiro valor
    def set_valor1(self, valor):
        # Converte o valor recebido para float e armazena
        self.__valor1 = float(valor)

    # Método para definir o segundo valor
    def set_valor2(self, valor):
        # Converte o valor recebido para float e armazena
        self.__valor2 = float(valor)

    # Método responsável por realizar o cálculo
    def calcular(self, operacao):

        # Estrutura match-case (similar ao switch do PHP)
        match operacao:

            # Caso a operação seja soma
            case "+":
                # Retorna a soma dos valores
                return self.__valor1 + self.__valor2

            # Caso a operação seja subtração
            case "-":
                # Retorna a subtração
                return self.__valor1 - self.__valor2

            # Caso a operação seja multiplicação
            case "*":
                # Retorna a multiplicação
                return self.__valor1 * self.__valor2

            # Caso a operação seja divisão
            case "/":
                # Verifica se o divisor é diferente de zero
                if self.__valor2 != 0:
                    # Retorna o resultado da divisão
                    return self.__valor1 / self.__valor2
                # Retorna mensagem de erro se for divisão por zero
                return "Erro: divisão por zero"

            # Caso a operação seja resto da divisão
            case "%":
                # Retorna o módulo
                return self.__valor1 % self.__valor2

            # Caso seja potência
            case "**":
                # Retorna valor1 elevado a valor2
                return self.__valor1 ** self.__valor2

            # Caso seja divisão inteira
            case "//":
                # Verifica divisão por zero
                if self.__valor2 != 0:
                    # Retorna divisão inteira
                    return self.__valor1 // self.__valor2
                # Retorna erro se divisor for zero
                return "Erro: divisão por zero"

            # Caso nenhuma operação seja válida
            case _:
                # Retorna mensagem padrão
                return "Operação inválida"