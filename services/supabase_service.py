import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Carrega as variáveis protegidas do arquivo .env
load_dotenv()

def get_supabase_client() -> Client:
    """Cria e retorna a instância de conexão com o Supabase."""
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    
    if not url or not key:
        raise ValueError("Credenciais do Supabase não encontradas no .env. Verifique o arquivo.")
        
    return create_client(url, key)

def fetch_unprocessed_contacts() -> list:
    """Busca os contatos que ainda não receberam a mensagem."""
    supabase = get_supabase_client()
    
    response = supabase.table("contatos").select("*").eq("processado", False).execute()
    
    return response.data