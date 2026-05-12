class ContaBancaria:
    def ativar_conta(self):
        self._ativo = True

conta3 = ContaBancaria("Carlos", 200)
print(f"Antes de ativar: Conta ativa? {conta3._ativo}")
conta3.ativar_conta()
print(f"Depois de ativar: Conta ativa? {conta3._ativo}")


class ContaBancaria:
    def __str__(self):
        return f"Conta de {self.titular} - Saldo: R${self.saldo}"

    conta1 = ContaBancaria("João", 1000)
    conta2 = ContaBancaria("Maria", 500)

    print(conta1)
    print(conta2)
