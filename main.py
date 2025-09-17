from pessoaFisica import PessoaFisica
from contaCorrente import ContaCorrente
from deposito import Deposito
from saque import Saque
from datetime import date



if __name__ == "__main__":

    cliente = PessoaFisica("1111111111111", "André Tozi", date(2006, 5, 25), "Rua Mackenzie, 110")

    conta = ContaCorrente.nova_conta(cliente, numero=1)
    cliente.adicionar_conta(conta)

    cliente.realizar_transacao(conta, Deposito(1000))

    cliente.realizar_transacao(conta, Saque(200))

    print("Saldo:", conta.saldo_atual())
    print("Histórico:", conta.historico.transacoes)
