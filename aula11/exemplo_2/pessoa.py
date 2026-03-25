class Pessoa:
    def __init__(self, nome, idade, cpf, email, telefone, endereco, cidade, estado):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
        self. telefone = telefone
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado

    def dados_formatados(self):
        return{
            "Nome": self.nome,
            "Idade": self.idade,
            "CPF": self.cpf,
            "E-mail": self.email,
            "Telefone": self.telefone,
            "Endereço": self.endereco,
            "cidade": self.cidade,
            "Estado": self.estado
        }