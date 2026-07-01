import json
import logging
import os
from socket import timeout

import requests

logger = loggin.getLogger(__name__)


#vai enviar o evento para o webhook do n8n visse
#ai se for true ele dale, caso não false se falhar (DESSE JEITO NÃO QUEBRA O FLUXO)
def enviar_evento_n8n(evento: str, payload: dict) -> bool:
    url = os.getenv("N8N_WEBHOOK_URL")
    timeout = int(os.getenv("N8N_TIMEOUT", 10))
    #timeout para que o tempo maximo do flask sobre o n8n, se passar desse tempo
    #o flask prossegue evitando ficar em loop de espera do n8n

    if not url:
        logger.error("N8N_WEBHOOK_URL não configurada no .env")
        return False

    body = {
        "evento": evento,
        "payload": payload,
        "origem": "backend-fluire"
    }

    try:
        response = request.post(
            url,
            json=body,
            timeout=timeout,
            headers = {"Content-type": "application/json"},
        )
        response.raise_for_status()
        return True

    except request.timeout:
        logger.error("Timeout ao enviar evento '%s' para n8n", evento )
        return False

    except request.RequestException as exc:
        logger.error("Falha ao enviar '%s' para n8n: '%s'", evento, exc)
        return False