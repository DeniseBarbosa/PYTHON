class ContaBancaria:
    def __init__(self, saldo_inicial):
        self._saldo = saldo_inicial

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, novo_saldo):
        if novo_saldo >= 0:
            self._saldo = novo_saldo
        else:
            print("O saldo não pode ser negativo!")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("Valor inválido para depósito!")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente para saque!")

# Criando uma conta com saldo inicial de 1000
minha_conta = ContaBancaria(100 )


# Verificando o saldo usando a propriedade (getter)
print("Saldo inicial:", minha_conta.saldo)

# Fazendo um depósito
minha_conta.depositar(0)
print("Saldo após depósito:", minha_conta.saldo)

# Fazendo um saque
minha_conta.sacar(50000)
print("Saldo após saque:", minha_conta.saldo)