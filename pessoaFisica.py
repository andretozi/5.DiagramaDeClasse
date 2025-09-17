from cliente import Cliente

class PessoaFisica(Cliente):
    def __init__(self, cpf: str, nome: str, data_nascimento, endereco: str):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
