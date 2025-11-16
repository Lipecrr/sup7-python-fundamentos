from typing import List
from rich.table import Table
from rich.console import Console

class Aluno():
    def __init__(
            self, 
            nome: str, 
            notas: List[float], 
            frequencia: float = 75, 
            turma: str = "SuperDev"
    ):
        self.nome = nome
        self.notas = notas
        self.frequencia = frequencia
        self.turma = turma


def exemplo_passagem_parametros_nomeados():
    # Pedro terá a frequencia de 75%, pq foi utilizado o valor default 
    # do parametro
    # # 2 parametros seguindo a ordem do contrutor e outro paramentro pelo 
    # nome (turma)
    pedro = Aluno("Pedro Silva", [8,7,6.5], turma = "SuperDev 7")

    # Passando todos os parametros pelo nomem podendo passar em qualquer ordem
    maria = Aluno(
        notas=[10, 9.75 , 3],
        nome="Maria",
        turma="Adas",
        frequencia=100 
    )


class Player:
    def __init__(
            self, 
            nick: str = "Geraldão", 
            classe: str = "Tanque", 
            lane: str = "Meio", 
            elo: str = "Bronze", 
            maestria: int = 7, 
            main: str = "Jinx"
            ):
        self.nick = nick
        self.classe = classe
        self.lane = lane
        self.elo = elo
        self.maestria = maestria
        self.main = main


def exercicio_player():
    orivundo = Player(
        nick="Orivundo", 
        classe="Atirador", 
        lane="bot"
        )
    lipecrr = Player(
        nick="Lipecrr", 
        elo="Esmeralda"
        )
    hamenon = Player(
        nick="Hamenon"
        )
    pedro = Player(
        nick="xXxPedrinSoloQVrauxXx", 
        classe="Lutador", lane="Mid", 
        elo="Bronze", 
        maestria=7
        )
    matheus = Player(
        nick="ZedGameplays", 
        classe="Assassino", 
        main="Zed", 
        elo="Ferro"
        )
    geraldao = Player(
        nick="Geraldão", 
        classe="Tanque", 
        lane="Top", elo="Mestre", 
        maestria=7, 
        main="Ornn"
        )
    vanderlei = Player(
        nick="Vandsgay", 
        main="Yummi"
        )

    table = Table(
        "Nick", 
        "Classe", 
        "Lane", 
        "Elo", 
        "Maestria", 
        "Main"
        )

    table.add_row(
        orivundo.nick,
        orivundo.classe,
        orivundo.lane,
        orivundo.elo,
        str(orivundo.maestria),
        orivundo.main
    )
    
    table.add_row(
        lipecrr.nick,
        lipecrr.classe,
        lipecrr.lane,
        lipecrr.elo,
        str(lipecrr.maestria),
        lipecrr.main
    )

    table.add_row(
        hamenon.nick,
        hamenon.classe,
        hamenon.lane,
        hamenon.elo,
        str(hamenon.maestria),
        hamenon.main
    )

    table.add_row(
        pedro.nick,
        pedro.classe,
        pedro.lane,
        pedro.elo,
        str(pedro.maestria),
        pedro.main
    )

    table.add_row(
        matheus.nick,
        matheus.classe,
        matheus.lane,
        matheus.elo,
        str(matheus.maestria),
        matheus.main
    )

    table.add_row(
        geraldao.nick,
        geraldao.classe,
        geraldao.lane,
        geraldao.elo,
        str(geraldao.maestria),
        geraldao.main
    )

    table.add_row(
        vanderlei.nick,
        vanderlei.classe,
        vanderlei.lane,
        vanderlei.elo,
        str(vanderlei.maestria),
        vanderlei.main
    )
    
    console = Console()
    console.print(table)

exercicio_player()


print("---------------------------------------------------------------------------")


class Produto:
    def __init__(
            self,
            preco: float, 
            nome: str="Sem nome", 
            categoria: str = "Geral", 
            estoque: int=0
            ):
        self.preco = preco
        self.nome = nome
        self.categoria = categoria
        self.estoque = estoque


def exercicio_02():
    pao = Produto(
        nome="Pão Frances", 
        preco=0.90, 
        categoria="Padaria", 
        estoque=200
        )
    carne = Produto(
        nome="Picanha", 
        preco=45.50, 
        categoria="Açougue"
        )

    table = Table(
        "Produto", 
        "Preço", 
        "Categoria", 
        "Estoque"
        )

    table.add_row(
        pao.nome,
        str(pao.preco),
        pao.categoria,
        str(pao.estoque)
    )

    table.add_row(
        carne.nome,
        str(carne.preco),
        carne.categoria,
        str(carne.estoque)
    )
    
    console = Console()
    console.print(table)


exercicio_02()


print("---------------------------------------------------------------------------")


class Carro:
    def __init__(
            self, 
            marca: str, 
            modelo: str, 
            ano: int, 
            cor: str="Branco", 
            portas: int=4, 
            motor: str="1.0", 
            cambio: str="Manual", 
            preco: float=0, 
            km: float=0, 
            usado: bool=False
            ):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.portas = portas
        self.motor = motor
        self.cambio = cambio
        self.preco = preco
        self.km = km
        self.usado = usado


def exercicio_03():
    corsa = Carro(
        marca="Chevrolet", 
        modelo="Corsa", 
        ano=1999, 
        cor="Prata", 
        portas=2, 
        motor="1.0", 
        cambio="Manual", 
        preco=7000.00, 
        km=264.23, 
        usado=True
        )
    fox = Carro(
        marca="Volkswagen", 
        modelo="Fox", 
        ano=2014, 
        portas=4, 
        motor="1.0", 
        cambio="Manual", 
        preco=40000.00, 
        km=64.23, 
        usado=True
        )

    table = Table(
        "Marca", 
        "Modelo", 
        "Ano", 
        "Cor", 
        "Portas", 
        "Motor", 
        "Cambio", 
        "Preço", 
        "KM", 
        "Usado"
        )

    table.add_row(
        corsa.marca,
        corsa.modelo,
        str(corsa.ano),
        corsa.cor,
        str(corsa.portas),
        corsa.motor,
        corsa.cambio,
        str(corsa.preco),
        str(corsa.km),
        str(corsa.usado)
    )

    table.add_row(
        fox.marca,
        fox.modelo,
        str(fox.ano),
        fox.cor,
        str(fox.portas),
        fox.motor,
        fox.cambio,
        str(fox.preco),
        str(fox.km),
        str(fox.usado)
    )

    console = Console()
    console.print(table)


exercicio_03()