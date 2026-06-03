from models.frequencias_model import *

def todas_listar_frequencias_service():
    return buscar_todas_frequencias()

def buscar_frequencias_aula_service(aula_id):
    return buscar_frequencias_por_aula_model(aula_id)

def buscar_frequencias_id_service(id):
    return buscar_frequencias_por_id_model(id)

def validar_presente_service(presente):
    if presente not in [0, 1]:
        raise Exception(
            "Valor de 'presente' deve ser 0 (ausente) ou 1 (presente)."
        )

def registrar_frequencias_service(aula_id, aluno_id, presente):
    validar_presente_service(presente)
    frequencias_existente = verificar_frequencias_existente(aula_id, aluno_id)
    if frequencias_existente:
        raise Exception("Frequência já registrada para este aluno nesta aula.")
    
    inserir_frequencias_model(aula_id, aluno_id, presente)
    return {
        "mensagem": "Frequência registrada com sucesso"
    }

def atualizar_frequencias_service(id, aula_id, aluno_id, presente):
    validar_presente_service(presente)
    frequencias_existente = verificar_frequencias_existente(aula_id, aluno_id)
    if not frequencias_existente:
        raise Exception("Frequência não encontrada para este aluno nesta aula.")
    
    atualizar_frequencias(id, presente)
    return {
        "mensagem": "Frequência atualizada com sucesso"
    }
    
def deletar_frequencias_service(id):
    frequencias = buscar_frequencias_por_id_model(id)

    if not frequencias:
        raise Exception("Frequência não encontrada.")
    
    deletar_frequencias_model(id)

    return {
        "mensagem": "Frequência deletada com sucesso"
    }