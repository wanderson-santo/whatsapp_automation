import pytest # type: ignore
from unittest.mock import patch
from services.zapi_service import send_whatsapp_message

@patch('services.zapi_service.requests.post')
def test_send_whatsapp_message_success(mock_post, monkeypatch):

    monkeypatch.setenv("ZAPI_INSTANCE", "instancia_teste")
    monkeypatch.setenv("ZAPI_TOKEN", "token_teste")
    monkeypatch.setenv("ZAPI_CLIENT_TOKEN", "client_token_teste")

    mock_post.return_value.status_code = 200

    result = send_whatsapp_message("5511999999999", "Marcelo")

    assert result is True
    
    # Verificando se o 'requests.post' foi chamado exatamente uma vez
    mock_post.assert_called_once()