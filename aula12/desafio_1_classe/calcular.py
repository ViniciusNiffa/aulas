# Define a classe Calcular
class Calcular:

    # Método construtor (executado quando o objeto é criado)
    def __init__(self):
        # Atributo privado valor1 iniciado com 0
        self.__valor1 = 0.0
        # Atributo privado valor2 iniciado com 0
        self.__valor2 = 0.0

    # Método GET para retornar valor1
    def get_valor1(self):
        # Retorna o valor armazenado em __valor1
        return self.__valor1

    # Método GET para retornar valor2
    def get_valor2(self):
        # Retorna o valor armazenado em __valor2
        return self.__valor2

    # Método SET para definir valor1
    def set_valor1(self, valor1):
        # Converte o valor recebido para float e armazena
        self.__valor1 = float(valor1)

    # Método SET para definir valor2
    def set_valor2(self, valor2):
        # Converte o valor recebido para float e armazena
        self.__valor2 = float(valor2)

    # Método para realizar soma
    def soma(self):
        # Calcula a soma dos dois valores
        resultado = self.__valor1 + self.__valor2
        # Retorna o resultado
        return resultado

    # Método para realizar subtração
    def subtracao(self):
        # Calcula a subtração
        resultado = self.__valor1 - self.__valor2
        # Retorna o resultado
        return resultado

    # Método para realizar multiplicação
    def multi(self):
        # Calcula a multiplicação
        resultado = self.__valor1 * self.__valor2
        # Retorna o resultado
        return resultado

    # Método para realizar divisão
    def div(self):
        # Verifica se o valor2 é diferente de zero
        if self.__valor2 != 0:
            # Realiza a divisão
            resultado = self.__valor1 / self.__valor2
        else:
            # Caso seja zero, retorna mensagem de erro
            return "Erro: divisão por zero"

        # Retorna o resultado
        return resultado