from transacao import Transacao

class Saque(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)
            return True
        return False
