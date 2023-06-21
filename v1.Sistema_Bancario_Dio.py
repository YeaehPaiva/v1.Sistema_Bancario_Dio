class SistemaBancario:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def depositar(self, valor):
        self.saldo += valor
        self.depositos.append(valor)

    def sacar(self, valor):
        if len(self.saques) >= 3 or valor > 500 or valor > self.saldo:
            return "Não foi possível realizar o saque devido a saldo insuficiente ou limite excedido."
        else:
            self.saldo -= valor
            self.saques.append(valor)
            return "Saque realizado com sucesso."

    def extrato(self):
        if not self.depositos and not self.saques:
            return "Nenhuma movimentação foi realizada."

        extrato = "Extrato:\n"
        for deposito in self.depositos:
            extrato += f"Depósito: R$ {deposito:.2f}\n"

        for saque in self.saques:
            extrato += f"Saque: R$ {saque:.2f}\n"

        extrato += f"Movimentações concluídas.\n"
        extrato += f"Saldo atual: R$ {self.saldo:.2f}"
        return extrato


# Função para exibir o menu e obter a opção escolhida pelo cliente
def exibir_menu():
    print("===== Menu =====")
    print("1. Sacar")
    print("2. Depositar")
    print("3. Extrato")
    print("4. Sair")

    opcao = input("Escolha uma opção (1-4): ")
    return opcao


# Função principal do programa
def main():
    banco = SistemaBancario()

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            valor = float(input("Digite o valor a sacar: "))
            resultado = banco.sacar(valor)
            print(resultado)
            print()
        elif opcao == "2":
            valor = float(input("Digite o valor a depositar: "))
            banco.depositar(valor)
            print("Depósito realizado com sucesso.")
            print()
        elif opcao == "3":
            extrato = banco.extrato()
            print(extrato)
            print()
        elif opcao == "4":
            print("Saindo do sistema bancário...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            print()


# Executar o programa
main()
