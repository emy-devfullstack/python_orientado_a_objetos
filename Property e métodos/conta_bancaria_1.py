class ContaBancaria:
    def ativar_conta(self):
        self._ativo = True

conta3 = ContaBancaria("Carlos", 200)
print(f"Antes de ativar: Conta ativa? {conta3._ativo}")
conta3.ativar_conta()
print(f"Depois de ativar: Conta ativa? {conta3._ativo}")
