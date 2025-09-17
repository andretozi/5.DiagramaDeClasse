from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, cliente, numero: int, limite: float = 500.0, limite_saques: int = 3):
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saques = limite_saques
        self.saques_realizados = 0

    def sacar(self, valor: float) -> bool:
        if self.saques_realizados >= self.limite_saques:
            print("Limite de saques atingido.")
            return False
        if valor > (self.saldo + self.limite):
            print("Saldo insuficiente incluindo limite.")
            return False
        if super().sacar(valor):
            self.saques_realizados += 1
            return True
        return False
