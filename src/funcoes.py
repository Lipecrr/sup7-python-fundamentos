def funcao_sem_retorno():
    print("Olá mundo")

def funcao_com_retorno() -> str:
    produto : str = "iPhone 17 Pro Max"
    return produto

def funcao_executar():
    funcao_sem_retorno()

    nome = funcao_com_retorno()
    print("Nome do produto: " + nome)




def solicitar_nome_jogo() -> str:
    nome : str = input("Digite o nome do jogo: ").strip()
    return nome

def solicitar_preco_jogo() -> float:
    preco : float = float(input("Digite o preço: "))
    return preco

def solicitar_quantidade_jogo() -> int:
    quantidade : int = int(input("Digite a quantidade: "))
    return quantidade

def solicitar_pedido_fechado() -> bool:
    pedido_fechado : str = input("Pedido fechado (s/n): ").strip().lower()
    if pedido_fechado == "s":
        return True
    else:
        return False

def solicitar_valor_pagamento():
    valor_pagamento : float = float(input("Digite o valor pago: "))
    return valor_pagamento

def processar_pedido():
    nome : str = solicitar_nome_jogo()
    preco : float = solicitar_preco_jogo()
    quantidade : int = solicitar_quantidade_jogo()
    pedido_fechado: bool = solicitar_pedido_fechado()

    valor_pedido : float = quantidade * preco
    print("\n\nValor pedido: " + str(valor_pedido))

    if pedido_fechado == True:
        valor_pagamento = solicitar_valor_pagamento()
        if valor_pagamento > valor_pedido:
            valor_troco = valor_pagamento - valor_pedido
            print("Troco: " + str(valor_troco))
            print("Status: Pedido realizado")
        elif valor_pagamento == valor_pedido:
            print("Pedido sem troco")
            print("Status: Pedido realizado")
        else:
            valor_faltante = valor_pedido - valor_pagamento
            print("Valor faltante: " + str(valor_faltante))
            print("Status: Pedido cancelado")


def solicitar_cotacao_dolar() -> float:
    cotacao : float = float(input("Digite o valor da contação do dolar hoje: ").replace("," , "."))
    return cotacao


def solicitar_nome_produto() -> str:
    nome = input("Digite o nome do produto: ")
    return nome


def solicitar_valor_produto_dolar() -> float:
    valor_dolar: float = float(input("Digite o valor do produto em dolar: ").replace("," , "."))
    return valor_dolar


def solicitar_se_pagara_imposto() -> bool:
    imposto: str = input("Pagara imposto (s/n): ").strip().lower()
    if imposto == "s":
        return True
    else:
        return False


def solicitar_deseja_utilizar_cota_dolar_mensal() -> bool:
    cota_mensal: str = input("Utilizara cota mensal de $500,00 (s/n): ").strip().lower()
    if cota_mensal == "s":
        return True
    else:
        return False

def calcular_valor_produto_acrescentando_imposto_utilizando_cota(
        valor_produto_dolar: float,
        cotacao_dolar: float,
        valor_produto_reais: float
):
    cotacao_mensal = 500.00
    # Calcular o valor que será utilizado para descobrir quanto a mais será pago de imposto
    valor_imposto_dolar = (valor_produto_dolar - cotacao_mensal) / 2
    valor_imposto_reais = valor_imposto_dolar * cotacao_dolar

    valor_total_produto_reais = valor_produto_reais + valor_imposto_reais
    print(f"""
Valor total do produto: $ {valor_produto_dolar}
Valor total do produto: R$ {valor_produto_reais}
Valor imposto: R$ {valor_imposto_reais}

Valor total do produto com imposto: R$ {valor_total_produto_reais}""")

def calcular_valor_produto_acrescentando_imposto(
    valor_produto_dolar: float,
    cotacao_dolar: float,
    valor_produto_reais: float
):
    valor_imposto_dolar = valor_produto_dolar / 2 # 50% de imposto
    valor_imposto_reais = valor_imposto_dolar * cotacao_dolar

    valor_total_produto_reais = valor_produto_reais + valor_imposto_reais
    print("Valor total do produto com imposto: " + str(valor_total_produto_reais))


def calcular_calor_compra_paraguai():
    cotacao_dolar : float = solicitar_cotacao_dolar()
    nome_produto : str = solicitar_nome_produto()
    valor_produto_dolar : float = solicitar_valor_produto_dolar()
    pagara_imposto : bool = solicitar_se_pagara_imposto()
    # Calcular o valor do produto em reais
    valor_produto_reais = valor_produto_dolar * cotacao_dolar
    if pagara_imposto == True:
        utilizar_cota_dolar_mensal = solicitar_deseja_utilizar_cota_dolar_mensal()

        if utilizar_cota_dolar_mensal == True:
            calcular_valor_produto_acrescentando_imposto_utilizando_cota(
                valor_produto_dolar, cotacao_dolar, valor_produto_reais,
            )
        else:
            calcular_valor_produto_acrescentando_imposto(
                valor_produto_dolar, cotacao_dolar, valor_produto_reais,
            )
    else:
        print("Valor do porduto sem pagar imposto: " + str(valor_produto_reais))

"""
Ex1: Criar função chamada exercicio_aluno
Solicitar o nome (criar função)
Solicitar a nota 1 (criar função)
Solicitar a nota 2 (criar função)
Solicitar a nota 3 (criar função)
calcular a média e apresentar
Criar um if que verifique se o aluno etá ou não aprovado e apresenar
Solicitar a idade (criar função)
solicitar o peso (criar função)
Solicitar a altura (criar função)
Calcular o IMC do aluno e apresentar a classificação
Aprensentar a geração de acordo com a idade
Solicitar o cargo (criar função)
Apresentar salário de acordo com cargo
 Estagiário R$ 850,00
 Junior R$ 1800,00
 Pleno R$ 4000,00
 Senior R$ 6000,00
"""
def solicitar_nome_aluno() -> str:
    nome = input("Digite o nome do aluno: ")
    return nome


def solicitar_nota1() -> float:
    nota = float(input("Digite a primeira nota: "))
    return nota


def solicitar_nota2() -> float:
    nota = float(input("Digite a segunda nota: "))
    return nota


def solicitar_nota3() -> float:
    nota = float(input("Digite a terceira nota: "))
    return nota


def calcular_media(
        nota1: float, nota2: float, nota3: float
) -> float:
    media = (nota1 + nota2 + nota3) / 3
    return media


def validar_situacao_aluno(media: float) -> str:
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"


def solicitar_idade_aluno() -> int:
    idade = int(input("Digite a idade do aluno: "))
    return idade

def solicitar_peso_aluno() ->float:
    peso = float(input("Digite o peso do aluno: "))
    return peso

def solicitar_altura_aluno() -> float:
    altura = float(input("Digite a altura do aluno: "))
    return altura

def calcular_imc(peso_aluno: float, altura_aluno: float) -> float:
    imc = peso_aluno / (altura_aluno * altura_aluno)
    return imc


def validar_geracao(idade_aluno: int) -> str:
    ano_nascimento = idade_aluno - 2025
    if ano_nascimento >= 1946 and ano_nascimento <= 1964:
        return "Baby Boomers"
    elif ano_nascimento >= 1965 and ano_nascimento <= 1980:
        return "Geração X"
    elif ano_nascimento >= 1981 and ano_nascimento <= 1996:
        return "Millennials"
    elif ano_nascimento >= 1997 and ano_nascimento <= 2012:
        return "Geração Z"
    elif ano_nascimento >= 2013:
        return "Geração Alpha"
    else:
        return "Geração Indefinida"


def solicitar_cargo() -> str:
    print(" Estagiário, Junior, Pleno ou Senior")
    cargo = input("Digite o cargo: ")
    return cargo


def validar_salario_cargo(cargo_aluno: str) -> float:
    if cargo_aluno.replace("á" , "a").strip == "estagiario":
        return 850.00
    elif cargo_aluno.strip == "junior":
        return 1800.00
    elif cargo_aluno.strip == "pleno":
        return 4000.00
    elif cargo_aluno.strip == "senior":
        return 6000.00


def exercicio_aluno ():
    nome_aluno: str = solicitar_nome_aluno()
    nota1: float = solicitar_nota1()
    nota2: float = solicitar_nota2()
    nota3: float = solicitar_nota3()
    media: float = calcular_media(nota1, nota2, nota3)
    situacao: str = validar_situacao_aluno(media)
    idade_aluno: int = solicitar_idade_aluno()
    peso_aluno: float = solicitar_peso_aluno()
    altura_aluno: float = solicitar_altura_aluno()
    imc_aluno: float = calcular_imc(peso_aluno, altura_aluno)
    geracao_aluno: str = validar_geracao(idade_aluno)
    cargo_aluno: str = solicitar_cargo()
    salario_cargo: float = validar_salario_cargo(cargo_aluno)

    print(f"""
Nome do aluno: {nome_aluno}
Media do aluno: {media:.2f}
Situação: {situacao}
Idade: {idade_aluno}
Peso: {peso_aluno}
Altura: {altura_aluno}
IMC: {imc_aluno}
Geração: {geracao_aluno}
Cargo: {cargo_aluno}
Salário: {salario_cargo}""")