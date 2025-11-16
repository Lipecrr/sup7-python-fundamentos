from datetime import date, datetime
import os
import platform
from typing import List
import questionary
from rich.table import Table
from rich.console import Console
from rich.align import Align


class Endereco:
    def __init__(self):
        self.cidade: str = None
        self.pais: str = None


class Jogo:
    def __init__(self):
        self.titulo: str = None
        self.data_lancamento: date = None
        self.preco: float = None
        self.genero: str = None
        self.classificacao: str = None
        self.desenvolvedora: "Desenvolvedora" = None


class Desenvolvedora:
    def __init__(self):
        self.nome: str = None
        self.sede: Endereco = None
        self.proprietario: str = None
        self.jogos: List["Jogo"] = []


def exemplo_01():
    endereco_rockstar = Endereco()
    endereco_rockstar.cidade = "Nova York"
    endereco_rockstar.pais = "US"

    rockstar_games = Desenvolvedora()
    rockstar_games.nome = "Rockstar Games"
    rockstar_games.proprietario = "Take-Two Interactive"
    rockstar_games.sede = endereco_rockstar

    gta_vi = Jogo()
    gta_vi.titulo = "GTA VI"
    gta_vi.data_lancamento = date(2077, 2, 28)
    gta_vi.preco = 669.99
    gta_vi.genero = "Ação"
    gta_vi.classificacao = "M"
    gta_vi.desenvolvedora = rockstar_games

    the_witcher = Jogo()
    the_witcher.titulo = "The Witcher 4"
    the_witcher.data_lancamento = date(2027, 12, 31)
    the_witcher.preco = 500
    the_witcher.genero = "RPG"
    the_witcher.classificacao = "M"

    league_of_legends = Jogo()
    league_of_legends.titulo = "League of Legends"
    league_of_legends.data_lancamento = date(2009, 10, 27)
    league_of_legends.preco = 0
    league_of_legends.genero = "Moba"
    league_of_legends.classificacao = "12"

    rockstar_games.jogos.extend([gta_vi, the_witcher, league_of_legends])

    colunas = ["Desenvolvedora", "Título", "Data Lançamento", "Preço", "Gênero", "Classificação"]
    tabela = Table(*colunas)

    tabela.add_row(
        gta_vi.desenvolvedora.nome,
        gta_vi.titulo,
        str(gta_vi.data_lancamento),
        f"R$ {gta_vi.preco:.2f}",
        gta_vi.genero,
        gta_vi.classificacao
    )
    tabela.add_row(
        "N/A",
        the_witcher.titulo,
        str(the_witcher.data_lancamento),
        f"R$ {the_witcher.preco:.2f}",
        the_witcher.genero,
        the_witcher.classificacao
    )
    tabela.add_row(
        "N/A",
        league_of_legends.titulo,
        str(league_of_legends.data_lancamento),
        f"R$ {league_of_legends.preco:.2f}",
        league_of_legends.genero,
        league_of_legends.classificacao
    )

    console = Console()
    console.print(tabela)


class Marca:
    def __init__(self):
        self.nome: str = None
        self.id: int = None
        self.fundador: str = None
        self.data_fundacao: date = None
        self.faturamento: float = None


def exercicio_marca():
    nike = Marca()
    nike.nome = "Nike"
    nike.id = 1
    nike.fundador = "Bill Bowerman e Phil Knight"
    nike.data_fundacao = date(1964, 1, 25)
    nike.faturamento = 51000000000.0

    adidas = Marca()
    adidas.nome = "Adidas"
    adidas.id = 2
    adidas.fundador = "Adolf Dassler"
    adidas.data_fundacao = date(1949, 8, 18)
    adidas.faturamento = 23683000000.0

    colunas = ["ID", "Marca", "Fundador", "Data Fundação", "Faturamento (US$)"]
    tabela = Table(*colunas)

    tabela.add_row(
        str(nike.id), nike.nome, nike.fundador, str(nike.data_fundacao), f"{nike.faturamento:,.2f}"
    )
    tabela.add_row(
        str(adidas.id), adidas.nome, adidas.fundador, str(adidas.data_fundacao), f"{adidas.faturamento:,.2f}"
    )

    console = Console()
    console.print(tabela)


class Usuario:
    def __init__(self):
        self.id: int = None
        self.nome_completo: str = None
        self.login: str = None
        self.data_nascimento: date = None


class Ticket:
    def __init__(self):
        self.numero: int = None
        self.usuario: Usuario = None
        self.data_abertura: date = None
        self.status: str = None
        self.data_fechamento: date = None
        self.descricao: str = None


def exercicio_ticket():
    felipe = Usuario()
    felipe.id = 1
    felipe.nome_completo = "Felipe Fernando Corrêa"
    felipe.login = "lipe@gmail.com"
    felipe.data_nascimento = date(1999, 2, 13)

    ana = Usuario()
    ana.id = 2
    ana.nome_completo = "Ana Paula da Silva Luz"
    ana.login = "ana@gmail.com"
    ana.data_nascimento = date(2001, 6, 13)

    ticket_felipe = Ticket()
    ticket_felipe.numero = 1001
    ticket_felipe.usuario = felipe
    ticket_felipe.data_abertura = date(2025, 11, 12)
    ticket_felipe.status = "Em análise"
    ticket_felipe.descricao = "Um homem muito belo e gentil"

    ticket_ana = Ticket()
    ticket_ana.numero = 1002
    ticket_ana.usuario = ana
    ticket_ana.data_abertura = date(2025, 11, 2)
    ticket_ana.status = "Finalizado"
    ticket_ana.data_fechamento = date(2025, 11, 12)
    ticket_ana.descricao = "Uma mulher muito bela e gentil"

    colunas = ["ID", "Usuário", "Login", "Data de Nascimento"]
    tabela = Table(*colunas)

    tabela.add_row(
        str(felipe.id), felipe.nome_completo, felipe.login, str(felipe.data_nascimento)
    )
    tabela.add_row(
        str(ana.id), ana.nome_completo, ana.login, str(ana.data_nascimento)
    )

    colunas2 = ["Número", "Usuário", "Abertura", "Fechamento", "Status", "Descrição"]
    tabela2 = Table(*colunas2)

    tabela2.add_row(
        str(ticket_felipe.numero),
        ticket_felipe.usuario.nome_completo,
        str(ticket_felipe.data_abertura),
        str(ticket_felipe.data_fechamento or ""),
        ticket_felipe.status,
        ticket_felipe.descricao
    )
    tabela2.add_row(
        str(ticket_ana.numero),
        ticket_ana.usuario.nome_completo,
        str(ticket_ana.data_abertura),
        str(ticket_ana.data_fechamento),
        ticket_ana.status,
        ticket_ana.descricao
    )

    console = Console()
    console.print(tabela)
    console.print(tabela2)


def limpar_tela():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")


console = Console()
desenvolvedoras: List[Desenvolvedora] = []


def menu_sistema():
    menu_geral = ""
    while menu_geral != "sair":
        menu_geral = questionary.select("Escolha o sistema", choices=["Desenvolvedora", "Sair"]).ask().lower()
        limpar_tela()
        if menu_geral == "desenvolvedora":
            exemplo_crud_lista_objetos()


def exemplo_crud_lista_objetos():
    menu = ""
    while menu != "sair":
        menu = questionary.select("Escolha o menu", choices=["Adicionar", "Listar", "Sair"]).ask().lower()
        limpar_tela()
        if menu == "adicionar":
            adicionar_desenvolvedora()
        elif menu == "listar":
            listar_desenvolvedoras()
        
# from rich.align import Align
 
def adicionar_desenvolvedora():
    # Solicitar os dados, instanciando um objeto de desenvolvedora e adicionar na lista
    console.print(Align.center("Cadastro de desenvolvedora"), style="blue")

    desenvolvedora = Desenvolvedora()
    desenvolvedora.nome = questionary.text("Digite o nome da desenvolvedora").ask()
    desenvolvedora.proprietario = questionary.text("Digite o nome do proprietário").ask()

    desenvolvedora.sede = Endereco()
    desenvolvedora.sede.cidade = questionary.text("Digite a cidade da sede").ask()
    desenvolvedora.sede.pais = questionary.text("Digite o país da sede").ask()

    desenvolvedoras.append(desenvolvedora)
    console.print("Desenvolvedora cadastrada com sucesso", style="green")
    input("Pressione ENTER para continuar...")
    limpar_tela()


def listar_desenvolvedoras():
    # Listar desenvolvedoras
    if len(desenvolvedoras) == 0:
        console.print("Nenhuma desenvolvedora cadastrada", style="red")
        input("Pressione ENTER para continuar...")
        limpar_tela()
        return

    table = Table("Nome", "Proprietário", "Endereço")

    for i in range(0, len(desenvolvedoras)):
        desenvolvedora = desenvolvedoras[i]
        table.add_row(
            desenvolvedora.nome,
            desenvolvedora.proprietario,
            f"{desenvolvedora.sede.pais} - {desenvolvedora.sede.cidade}"
        )
    
    
    console.print(table)

# exemplo_crud_lista_objetos()

class Dono:
    def __init__(self):
        self.nome: str = None
        self.cpf: str = None
        self.bairro: str = None
        self.rua: str = None
        self.numero: int = None


class Animal:
    def __init__(self):
        self.raca: str = None
        self.dono: Dono = None
        self.data_nascimento: date = None
        self.peso: float = None
        self.altura: float = None
        self.sexo: str = None
        self.cor: str = None
        self.origem_raca: str = None


animais: List[Animal] = []


def menu_sistema():
    menu_geral = ""
    while menu_geral != "sair":
        menu_geral = questionary.select("Escolha o sistema", choices=["Animais", "Sair"]).ask().lower()
        limpar_tela()
        if menu_geral == "animais":
            crud_lista_animais()


def crud_lista_animais():
    menu = ""
    while menu != "sair":
        menu = questionary.select("Escolha o menu", choices=["Adicionar", "Listar", "Sair"]).ask().lower()
        limpar_tela()
        if menu == "adicionar":
            adicionar_animais()
        elif menu == "listar":
            listar_animais()


def adicionar_animais():
    console.print("Cadastro de animal")

    animal = Animal()
    animal.raca = questionary.text("Digite o nome da raça").ask()
    data_str = input("Digite a data de nascimento (DD/MM/AAAA)")
    animal.data_nascimento = datetime.strptime(data_str, "%d/%m/%Y")
    animal.peso = float(input("Digite o peso"))
    animal.altura = float(input("Digite a altura"))
    animal.sexo = questionary.text("Digite o sexo").ask()
    animal.cor = questionary.text("Digite a cor do animal").ask()
    animal.origem_raca = questionary.text("Digite a origem da raça").ask()

    animal.dono = Dono()
    animal.dono.nome = questionary.text("Digite o nome do dono").ask()
    animal.dono.cpf = questionary.text("Digite o CPF").ask()
    animal.dono.bairro = questionary.text("Digite o bairro").ask()
    animal.dono.rua = questionary.text("Digite a rua").ask()
    animal.dono.numero = int(input("Digite o numero"))

    animais.append(animal)
    console.print("Animal cadastrada com sucesso")
    input("Pressione ENTER para continuar...")
    limpar_tela()


def listar_animais():
    if len(animais) == 0:
        console.print("Nenhum animal cadastrado")
        input("Pressione ENTER para continuar...")
        limpar_tela()
        return

    table = Table("Raça", "Data de nascimento", "Peso", "Altura", "Sexo", "Cor", "Origem da Raça", "Dono", "CPF do dono", "Bairro", "Rua", "Número")

    for i in range(0, len(animais)):
        animal = animais[i]
        table.add_row(
            animal.raca,
            str(animal.data_nascimento),
            str(animal.peso),
            str(animal.altura),
            animal.sexo,
            animal.cor,
            animal.origem_raca,
            animal.dono.nome,
            animal.dono.cpf,
            animal.dono.bairro,
            animal.dono.rua,
            str(animal.dono.numero)
        )
    
    
    console.print(table)

crud_lista_animais()