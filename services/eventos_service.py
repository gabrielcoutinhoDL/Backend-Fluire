import json
import logging

from services.n8n_service import enviar_evento_n8n
from models.notificacoes_model import NotificacoesModel

logger = logging.getLogger(__name__)

# Eventos previstos (constantes para evitar typos)
EVENTO_ALUNO_CADASTRADO = "aluno_cadastrado"
EVENTO_ALUNO_FALTOU = "aluno_faltou"
EVENTO_ALUNO_INATIVO = "aluno_inativo"
EVENTO_FREQUENCIA_BAIXA = "frequencia_baixa"
EVENTO_AULA_PROXIMA = "aula_proxima"
EVENTO_LEMBRETE_AULA = "lembrete_aula"
EVENTO_RECUPERACAO_SENHA = "recuperacao_senha_solicitada"


def disparar_evento(evento: str, payload: dict, aluno_id=None, usuario_id=None) -> bool:
    
    #Dispara evento para n8n e registra histórico.
    #Falha no n8n NÃO propaga exceção — apenas log + status 'falhou'.
    
    notificacao_id = NotificacoesModel.registrar(
        tipo=evento,
        aluno_id=aluno_id,
        usuario_id=usuario_id,
        status="pendente",
        payload_json=json.dumps(payload, ensure_ascii=False, default=str),
    )

    sucesso = enviar_evento_n8n(evento, payload)
    status = "enviado" if sucesso else "falhou"

    NotificacoesModel.atualizar_status(notificacao_id, status)

    if not sucesso:
        logger.warning("Evento '%s' registrado como falhou (id=%s)", evento, notificacao_id)

    return sucesso