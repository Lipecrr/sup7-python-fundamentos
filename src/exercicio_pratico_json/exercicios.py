from src.arquivos import ler_json, escrever_json
from typing import Dict, List

def exercicio_01():
    usuarios: List[Dict[str, any]] = ler_json("data/usuarios.json")

    free = []

    for i in range(0, len(usuarios)):
        usuario = usuarios[i]
        assinatura = usuario.get("assinatura", {})
        plano = assinatura.get("plano")

        dados_pessoais = usuario.get("dados_pessoais")
        nome = dados_pessoais.get("nome")

        if plano == "Free":
            free.append(nome)

    escrever_json(free, "data/free.json")


def exercicio_02():
    usuarios: List[Dict[str, any]] = ler_json("data/usuarios.json")

    tags = []

    for i in range(0, len(usuarios)):
        usuario = usuarios[i]

        tags_usuario = usuario.get("tags")
        for i in range(0, len(tags_usuario)):
            tags.append(tags_usuario[i])

    escrever_json(tags, "data/tags.json")


def exercicio_03():
    usuarios: List[Dict[str, any]] = ler_json("data/usuarios.json")

    enderecos = []

    for i in range(0, len(usuarios)):
        usuario = usuarios[i]
        endereco = usuario.get("endereco")
        rua = endereco.get("rua")
        numero = endereco.get("numero")
        bairro = endereco.get("bairro")
        cep = endereco.get("cep")
        uf = endereco.get("uf")

        dados = [rua, numero, bairro, cep, uf]
        enderecos.append(dados)

    escrever_json(enderecos, "data/enderecos.json")


def exercicio_04():
    usuarios: List[Dict[str, any]] = ler_json("data/usuarios.json")

    sp, rj, pr ,mg ,sc ,rs ,pe ,ce ,ba ,am ,df = [], [], [], [], [], [], [], [], [], [], []

    for i in range(0, len(usuarios)):
        usuario = usuarios[i]
        endereco = usuario.get("endereco")
        uf = endereco.get("uf")

        dados_pessoais = usuario.get("dados_pessoais")
        email = dados_pessoais.get("email")
        telefone = dados_pessoais.get("telefone")

        dados = {
            "email": email,
            "telefone": telefone
        }
        if uf == "SP":
            sp.append(dados)
        elif uf == "RJ":
            rj.append(dados)
        elif uf == "PR":
            pr.append(dados)
        elif uf == "MG":
            mg.append(dados)
        elif uf == "SC":
            sc.append(dados)
        elif uf == "RS":
            rs.append(dados)
        elif uf == "PE":
            pe.append(dados)
        elif uf == "CE":
            ce.append(dados)
        elif uf == "BA":
            ba.append(dados)
        elif uf == "AM":
            am.append(dados)
        elif uf == "DF":
            df.append(dados)

    escrever_json(sp, "data/sp.json")
    escrever_json(rj, "data/rj.json")
    escrever_json(pr, "data/pr.json")
    escrever_json(mg, "data/mg.json")
    escrever_json(sc, "data/sc.json")
    escrever_json(rs, "data/rs.json")
    escrever_json(pe, "data/pe.json")
    escrever_json(ce, "data/ce.json")
    escrever_json(ba, "data/ba.json")
    escrever_json(am, "data/am.json")
    escrever_json(df, "data/df.json")