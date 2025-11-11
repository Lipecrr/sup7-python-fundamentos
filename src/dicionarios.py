from typing import Dict, Union


def exemplo_dicionario_basico():
    # Dicionário é uma forma de armazenar chaves e valores
    # Cada chave está atrelado a um valor

    # Dicionário terá uma chave do tipo string
    # Pode armazenar string, int ou bool
    # Criarmos um dicionário com 2 chaves (apelido, idade)
    cachorro: Dict[str, Union[str, int, bool, float]] = {
        "apelido": "Tobby",
        "idade": 4,
        "abandonado": True,
        "peso": 22.5
    }

    # Acrescentar uma nova chave com um valor
    cachorro["raca"] = "Pastor Alemão"

    cachorro["cor"] = "Caramelo"

    # Alterar o valor de uma chave
    cachorro["idade"] = 5

    # Remover uma chave(automaticamente remove o valor)
    cachorro.pop("abandonado")

    # Print("Cachorro:", cachorro["apelido"])
    print(f"""
Cachorro: {cachorro.get("apelido")}
Raça: {cachorro.get("raca")}
Idade: {cachorro.get("idade")}
Cor: {cachorro.get("cor")}
Abandonado: {cachorro.get("abandonado")}
Peso: {cachorro.get("peso")}""")
    
# Exercicio 01:
# Criar uma função exemplo_dicionario_aluno()
# Criar um dicionario chamado aluno com os seguintes dados
#  nome_completo
#  noma_mae
#  nome_pai
# jogar (true)
# Apresentar os dado do dicionario
# Adicionar a chave idade do aluno
# Apresentar a idade do aluno
# Alterar a idade do aluno para +1
# Remover a chave jogar do aluno
# Apresentar os dados


def exemplo_dicionario_aluno():
    aluno: Dict[str, Union[str, int, bool, float]] = {
        "nome_completo": "Felipe Fernando Corrêa",
        "noma_mae": "Luciana Xavier",
        "nome_pai": "Fabio Fernando Corrêa",
        "jogar": True,
    }

    print(f"""
Nome Completo: {aluno.get("nome_completo")}
Nome da mãe: {aluno.get("nome_mae")}
Nome do pai: {aluno.get("nome_pai")}
Joga: {aluno.get("jogar")}""")
    
    aluno["idade"] = 26

    print(f"""
Nome Completo: {aluno.get("nome_completo")}
Nome da mãe: {aluno.get("nome_mae")}
Nome do pai: {aluno.get("nome_pai")}
Joga: {aluno.get("jogar")}
Idade: {aluno.get("idade")}""")
    
    aluno["idade"] = aluno["idade"] + 1
    aluno.pop("jogar")

    print(f"""
Nome Completo: {aluno.get("nome_completo")}
Nome da mãe: {aluno.get("nome_mae")}
Nome do pai: {aluno.get("nome_pai")}
Joga: {aluno.get("jogar")}
Idade: {aluno.get("idade")}""")