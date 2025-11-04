from dotenv import load_dotenv
from os import getenv

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Carrega as variáveis de dentro do arquivo .env as caráveis de ambiente
load_dotenv()

def obter_login() -> str:
    email = getenv("EMAIL")
    if email is None:
        raise Exception("Login não está preenchido no arquivo .env")
    
    return email


def obter_senha() -> str:
    senha = getenv("SENHA")
    if senha is None:
        raise Exception("Login não está preenchido no arquivo .env")
    
    return senha


def enviar(destinatario: str, corpo: str):
    mensagem = MIMEMultipart()
    mensagem["From"] = _obter_login()
    mensagem["To"] = destinatario
    mensagem["Subject"] = "Pedido criado"

    mensagem.attach(MIMEText(corpo, "plain"))

    try:
        with smtplib.SMTP("smtp.gamil.com", 587) as servidor:
            servidor.starttls() # Criptografia da conexão
            servidor.login(_obter_login(), _obter_senha())
            servidor.send_message(mensagem)
            print("✅ E-mail enviado com sucesso")
    except Exception as e:
        print("❌ Erro ao enviar e-mail: ", e)

    
def enviar_email_pedido(destinatario: str, tamanho: str, sabores: list[str]):
    mensagem = f"""Pedido criado com sucesso!

    Tamanho da pizza: {tamanho}
    Sabores: {",".join(sabores)}    
    """

    enviar(destinatario, mensagem)






print(obter_login())