import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

def send_whatsapp_message(phone: str, name: str) -> bool: # pyright: ignore[reportReturnType]
    """Envia a mensagem via Z-API para o contato especificado."""
    
    instance = os.environ.get("ZAPI_INSTANCE")
    token = os.environ.get("ZAPI_TOKEN")
    client_token = os.environ.get("ZAPI_CLIENT_TOKEN")

    if not all([instance, token, client_token]):
        raise ValueError("Credenciais da Z-API ausentes no .env.")

    # URL padrão de envio de texto da Z-API
    url = f"https://api.z-api.io/instances/{instance}/token/{token}/send-text"

    # Mensagem exata exigida no desafio
    message = f"Olá, {name} tudo bem com você?"

    headers = {
        "Client-Token": client_token,
        "Content-Type": "application/json"
    }

    payload = {
        "phone": phone,
        "message": message
    }

    # Disparo HTTP via biblioteca requests
    response = requests.post(url, json=payload, headers=headers)

    # Verifica se a requisição retornou Status Code 200 ou 201
    if response.status_code in [200, 201]:
        return True
    else:
        # Lança uma exceção detalhada caso a API recuse o envio
        response.raise_for_status()