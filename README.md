# Desafio Técnico - b2bflow ⚡

Projeto desenvolvido para a 1ª etapa do processo seletivo de Estágio em Desenvolvimento Python. O script lê contatos não processados de um banco de dados no Supabase e envia uma mensagem personalizada via WhatsApp utilizando a Z-API.

## ⚙️ Setup do Banco de Dados (Supabase)
Execute o seguinte DDL na aba SQL Editor do seu projeto Supabase para criar a tabela necessária:

```sql
CREATE TABLE contatos (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  telefone VARCHAR(20) NOT NULL,
  processado BOOLEAN DEFAULT FALSE
);
```

# 🔐 Variáveis de Ambiente (.env)
Crie um arquivo .env na raiz do projeto com as seguintes variáveis:
```
SUPABASE_URL=sua_url_do_supabase
SUPABASE_KEY=sua_anon_key_do_supabase
ZAPI_INSTANCE=sua_instancia_zapi
ZAPI_TOKEN=seu_token_zapi
ZAPI_CLIENT_TOKEN=seu_client_token_zapi
```
# 🚀 Como Rodar o Projeto
Clone este repositório.

Crie e ative um ambiente virtual (python -m venv venv e source venv/bin/activate).

Instale as dependências: pip install -r requirements.txt.

Execute o script principal: python main.py.
