from datetime import date
from typing import List
from rich.table import Table
from rich.console import Console

class Cachorro:
    #Contrutor
    def __init__(self, raca_param: str, peso: float, idade: int, cor: str = "Caramelo"):
        # Atributos são peenchidos com os dados dos parametros
        #o parametro cor tem um valor default(padrão) que é "Caramelo"
        self.raca = raca_param
        self.peso = peso
        self.idade = idade
        self.cor = cor
        #Atributo com valor pré-definido
        self.cidade_natal = "Blumenau"


def exemplo_construtor_cachorro():
# Cachorro (raca, peso, idade)
    tobby = Cachorro("Dobberman", 45.20, 15, "Preto")
    print("Raça", tobby.raca)
    print("Peso", tobby.peso)
    print("Idade", tobby.idade)
    print("Cidade natal", tobby.cidade_natal)
    print("Cor", tobby.cor)

    # Instanciar um objeto chama
    daschund = Cachorro("Salsicha", 70.00, 5)
    print("Raça", daschund.raca)
    print("Peso", daschund.peso)
    print("Idade", daschund.idade)
    print("Cidade natal", daschund.cidade_natal)
    print("Cor", daschund.cor)
    

class Passagem:
    def __init__(self, destino: str, quantidade_dias: int, data_inicio: str, quantidade_pessoas: int = 2, partida: str = "São Paulo"):
        self.destino = destino
        self.quantidade_dias = quantidade_dias
        self.data_inicio = data_inicio
        self.quantidade_pessoas = quantidade_pessoas
        self.partida = partida


def exercicio_passagem():
    felipe = Passagem("Texas", 20, "23/12/2025")

    ana = Passagem("Canada", 15, "13/04/2025")

    fernando = Passagem("Mexico", 34, "23/11/2026", 3)

    paula = Passagem("Chile", 23, "30/04/2027", 6, "Navegantes")

    table = Table("Destino", "Quantidade de dias", "Inicio da viagem", "Quantidade de pessoas", "Partida")

    table.add_row(
        felipe.destino,
        str(felipe.quantidade_dias),
        felipe.data_inicio
        )
    
    table.add_row(
        ana.destino,
        str(ana.quantidade_dias),
        ana.data_inicio
    )

    table.add_row(
        fernando.destino,
        str(fernando.quantidade_dias),
        fernando.data_inicio,
        str(fernando.quantidade_pessoas)
    )

    table.add_row(
        paula.destino,
        str(paula.quantidade_dias),
        paula.data_inicio,
        str(paula.quantidade_pessoas),
        paula.partida
    )
    
    console = Console()
    console.print(table)


exercicio_passagem()