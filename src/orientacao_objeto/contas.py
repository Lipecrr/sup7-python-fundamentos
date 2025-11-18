class Conta:
    def __init__(self, titular: str, saldo_inicial: float):
        """Construtor da classe. Inicializa o titular e o saldo"""
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor_deposito: float):
        """Adiciona um valor ao saldo da conta."""
        if valor_deposito <= 0:
            print(f"DEPÓSITO: Valor do depósito inválido R$ {valor_deposito:.2f}.")            
            return

        self.saldo = self.saldo + valor_deposito
        print(f"DEPÓSITO: Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")

    def sacar(self, valor_saque: float):
        """Remove um valor do saldo da conta, se houver dinheiro suficiente"""
        if valor_saque > self.saldo:
            print(f"SAQUE: Saldo insuficiente para realizar o saque de R$ {valor_saque:.2f}.")
        else:
            self.saldo = self.saldo - valor_saque
            print(f"SAQUE: Saque de R$ {self.saldo:.2f}")

    def exibir_saldo(self):
        """Mostra o status atual da conta"""
        print(f"EXTRATO: Saldo Atual de R$ {self.saldo:.2f}.")


def exemplo_conta():
    """Método para testar a funcionalidade da conta"""
    conta_bradesco = Conta("Vitor", 3900.22)

    conta_bradesco.exibir_saldo()
    conta_bradesco.depositar(100.78) #3100.22
    conta_bradesco.depositar(-10)

    conta_bradesco.sacar(4000) #Não permitir pois saldo insuficiente
    conta_bradesco.sacar(3500) #Não permitir pois saldo insuficiente

    conta_bradesco.sacar(3201)
    conta_bradesco.exibir_saldo()


# exemplo_conta()


class Aluno:
    def __init__(self, nome: str):
        self.nome = nome
        self.notas = []
        self.media = 0

    def adicionar(self, nota: float):
        self.notas.append(nota)

    def apresentar_notas(self):
        i = 0
        for nota in self.notas:
            print(f"Nota {i + 1}:", nota)
            i += 1

    def calcular_media(self):
        soma = 0
        for nota in self.notas:
            soma += nota
        
        self.media = soma / len(self.notas)

def exercicio_aluno():
    felipe = Aluno("Felipe")
    felipe.adicionar(9.3)
    felipe.adicionar(8.9)
    felipe.adicionar(9.6)
    felipe.apresentar_notas()
    
    felipe.calcular_media()

    print(f"A Media do aluno {felipe.nome}: {felipe.media:.2f}")

exercicio_aluno()
