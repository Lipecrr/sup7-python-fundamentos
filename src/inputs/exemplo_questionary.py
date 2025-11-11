# from questionary import text, password, select, checkbox, confirm
# from src.envios.envio_email import enviar_email_pedido


# sabores_pizza = [
#     "Calabresa",
#     "Mussarela",
#     "Frango com Catupiry",
#     "Portuguesa",
#     "Quatro Queijos",
#     "Marguerita",
#     "Pepperoni",
#     "Bacon",
#     "Napolitana",
#     "Vegetariana"
# ]


# def _solicitar_text() -> str:
#     cliente = text("Digite o e-mail do cleinte").ask()
#     return cliente


# def _solicitar_senha() -> str:
#     senha = password("Digite a senha do cliente").ask()
#     return senha


# def _escolher_opcao() -> str:
#     opcoes = ["Pequena", "Média", "Grande"]
#     opcao_escolhida = select("Escolha o tamanho da pizza", choices=opcoes).ask()
#     return opcao_escolhida


# def _escolher_sabores(tamanho: str) -> list:
#     quantidade_maxima_sabores = 1
#     if tamanho == "Médio":
#         quantidade_maxima_sabores = 2
#     elif tamanho == "Grande":
#         quantidade_maxima_sabores = 4

#     sabores = checkbox(
#         "Escolha o(s) sabor(es) desejado(s)",
#         choices=sabores_pizza,
#         validate=lambda elementos: _validar_quantidade_sabores(elementos, quantidade_maxima_sabores)
#     ).ask()

#     return sabores
    

# def _validar_quantidade_sabores(elementos: list[str], quantidade_maxima: int) -> bool | str:
#     if len(elementos) == 0:
#         return "No mínimo deve conter 1 sabor"
#     if len(elementos) > quantidade_maxima:
#         return f"A pizza deve conter no máximo {quantidade_maxima} sabor(es)"
#     return True


# def _solicitar_confirmacao() -> bool:
#     confirmado = confirm("Você confirma o pedido?").ask()
#     return confirmado


# def exemplos():
#     cliente = _solicitar_text()
#     senha = _solicitar_senha()

#     if cliente.endswith("@proway.com") and senha == "batatinha":
#         tamanho = _escolher_opcao()
#         sabores = _escolher_sabores(tamanho)
#         pedido_confirmado = _solicitar_confirmacao()

#         if pedido_confirmado == True:
#             enviar_email_pedido(cliente, tamanho, sabores)
#             print("Pedido confirmado")
#         else:
#             print("Pedido cancelado")
