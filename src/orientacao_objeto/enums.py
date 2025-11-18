from enum import Enum
from rich.table import Table
from rich.console import Console

# Region Console
class MarcaEnum(Enum):
    SONY = "Sony"
    MICROSOFT = "Microsoft"


class Console:
    def __init__(self):
        self.marca: MarcaEnum
        self.modelo: str = ""


def exemplo_consoles():
    # Iniciar um objeto
    play_station = Console()
    play_station.marca = MarcaEnum.SONY
    play_station.modelo = "PS1"

    play_station_2 = Console()
    play_station_2.marca = MarcaEnum.SONY
    play_station_2.modelo = "PS2"

    xbox = Console()
    xbox.marca = MarcaEnum.MICROSOFT
    xbox.modelo = "Xbox"
# Endregion


class PessoaTipo(Enum):
    FISICA = "PF"
    JURIDICA = "PJ"


class Pessoa:
    def __init__(self):
        self.nome: str
        self.cpf_cnpj: str
        self.tipo: PessoaTipo


def exemplo_pessoas():
    creber = Pessoa()
    creber.nome = "Cleiton"
    creber.cpf_cnpj = "23.433.543/0001-01"
    creber.tipo = PessoaTipo.JURIDICA

    print(
        "PESSOA:",
        creber.nome,
        "CPF/CNPJ",
        creber.cpf_cnpj,
        "TIPO:",
        creber.tipo.value,
    )



class PersonagemEnum(Enum):
    BATMAN = "Batman"
    SUPERMAN = "Superman"
    BUZZ_LIGHTYEAR = "Buzz Lightyear"
    HOMEM_FORMIGA = "Homem Formiga"
    BOB_ESPONJA = "Bob Esponja"
    CAT_DOG = "Cat Dog"


class StatusEnum(Enum):
    PENDENTE = "Pendente"
    EM_ANDAMENTO = "Em andamento"
    CANCELADO = "Cancelado"
    FINALIZADO = "Finalizado"


class Job:
    def __init__(self):
        self.personagem: PersonagemEnum
        self.valor: float
        self.local_atuacao: str
        self.status: StatusEnum


def exercicio_personagem():
    personagem_01 = Job()
    personagem_01.personagem = PersonagemEnum.BATMAN
    personagem_01.valor = 666.66
    personagem_01.local_atuacao = "Gothan"
    personagem_01.status = StatusEnum.EM_ANDAMENTO

    personagem_02 = Job()
    personagem_02.personagem = PersonagemEnum.BOB_ESPONJA
    personagem_02.valor = 231.54
    personagem_02.local_atuacao = "Siri cascudo"
    personagem_02.status = StatusEnum.FINALIZADO

    print(
        "\n\nPERSONAGEM:",
        personagem_01.personagem.value,
        "\nVALOR:",
        str(personagem_01.valor),
        "\nLOCAL DE ATUAÇÃO:",
        personagem_01.local_atuacao,
        "\nSTATUS:",
        personagem_01.status.value,
    )

    print(
        "\n\nPERSONAGEM:",
        personagem_02.personagem.value,
        "\nVALOR:",
        str(personagem_02.valor),
        "\nLOCAL DE ATUAÇÃO:",
        personagem_02.local_atuacao,
        "\nSTATUS:",
        personagem_02.status.value,
    )



if __name__ == "__main__":
    exemplo_pessoas()
    exercicio_personagem()