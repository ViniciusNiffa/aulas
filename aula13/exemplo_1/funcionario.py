class Funcionario:
    def __init__(self):
        self.__nome = ""
        self.__salario_bruto = 0.0
        self.__vale_alimentacao = 0.0
        self.__vale_transporte = 0.0

        self.__inss = 0.0
        self.__ir = 0.0
        self.__desconto_va = 0.0
        self.__desconto_vt = 0.0

    def set_nome(self, nome):
        self.__nome = nome.strip()
    def set_salario_bruto(self, valor):
        self.__salario_bruto = float(valor)
    def set_vale_alimentacao(self, valor):
        self.__vale_alimentacao = float(valor)
    def set_vale_transporte(self, valor):
        self.__vale_transporte = float(valor)
    
    def get_nome(self):
        return self.__nome
    def get_salario_bruto(self):
        return self.__salario_bruto
    def get_inss(self):
        return self.__inss
    def get_ir(self):
        return self.__ir
    def get_desconto_va(self):
        return self.__desconto_va
    def get_desconto_vt(self):
        return self.__desconto_vt
    
    # Cálculo do INSS
    def calcular_inss(self):
        if self.__salario_bruto <= 1320:
            self.__inss = self.__salario_bruto * 0.075
        elif self.__salario_bruto <= 2571:
            self.__inss = self.__salario_bruto * 0.09
        elif self.__salario_bruto <= 3856:
            self.__inss = self.__salario_bruto*0.12
        else:
            self.__inss = self.__salario_bruto*0.14
        
        return self.__inss
    
    # Cálculo do IR simplificado
    def calcular_ir(self):
        base = self.__salario_bruto - self.__inss

        if base <= 2112:
            self.__ir = 0
        elif base <= 2826:
            self.__ir = base * 0.075
        elif base <= 3751:
            self.__ir = base * 0.15
        elif base <= 4664:
            self.__ir = base * 0.225
        else:
            self.__ir = base * 0.275
        
        return self.__ir
    # Cálculo do desconto do vale alimentação
    def calcular_vale_alimentacao(self):
        # 6% sobre o valor recebido de vale
        self.__desconto_va = self.__vale_alimentacao * 0.06
        return self.__desconto_va
    
    #Cálculo do desconto Vale transporte
    def calcular_vale_transporte(self):
        # 6% sobre o salário bruto
        desconto_calculado = self.__salario_bruto * 0.06

        # Desconto não pode ser maior que o valor recebido de VT
        if desconto_calculado > self.__vale_transporte:
            self.__desconto_vt = self.__vale_transporte
        else:
            self.__desconto_vt = desconto_calculado
            
        return self.__desconto_vt
    
    # Cálculo final do salário líquido
    def calcular_salario_liquido(self):
        self.calcular_inss()
        self.calcular_ir()
        self.calcular_vale_alimentacao()
        self.calcular_vale_transporte()

        total_descontos = (
            self.__inss +
            self.__ir +
            self.__desconto_va +
            self.__desconto_vt
        )
        liquido = self.__salario_bruto - total_descontos

        return liquido