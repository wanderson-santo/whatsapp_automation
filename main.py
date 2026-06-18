import logging
from services.supabase_service import fetch_unprocessed_contacts
from services.zapi_service import send_whatsapp_message

# Configurando os logs (Boas Práticas)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Iniciando o processamento de contatos...")
    
    try:
        # Busca os contatos no banco
        contacts = fetch_unprocessed_contacts()
        
        if not contacts:
            logging.info("Nenhum contato pendente para envio encontrado.")
            return

        # Itera sobre os contatos retornados
        for contact in contacts:
            name = contact.get("nome")
            phone = contact.get("telefone")
            
            logging.info(f"Tentando enviar mensagem para {name} ({phone})...")
            
            try:
                # Dispara a mensagem
                success = send_whatsapp_message(phone, name)
                
                if success:
                    logging.info(f"[SUCESSO] Mensagem enviada para {name}.")
            
            except Exception as e:
                # Se a Z-API falhar, o script não quebra abruptamente
                logging.error(f"[ERRO] Falha ao enviar para {name}: {e}")
                
    except Exception as e:
        # Se o Supabase cair, o erro é capturado aqui
        logging.error(f"[ERRO FATAL] Falha de conexão com o banco de dados: {e}")

if __name__ == "__main__":
    main()