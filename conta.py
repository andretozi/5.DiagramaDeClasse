from historico import Historico

class Conta:
    def __init__(self, cliente, numero: int, agencia: str = "0001"):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def saldo_atual(self):
        return self.saldo

    @classmethod
    def nova_conta(cls, cliente, numero: int):
        return cls(cliente, numero)

    def sacar(self, valor: float) -> bool:
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            return True
        return False

    def depositar(self, valor: float) -> bool:
        if valor > 0:
            self.saldo += valor
            return True
        return False
