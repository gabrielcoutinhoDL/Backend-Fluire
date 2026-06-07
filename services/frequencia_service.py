from models.frequencias_model import *

def todas_listar_frequencias_service():
    return buscar_todas_frequencias()

def buscar_frequencias_aula_service(aula_id):
    return buscar_frequencias_por_aula(aula_id)

def validar_presente_service(presente):
    if presente not in [0, 1]:
        raise Exception("Valor de 'presente' deve ser 0 (ausente) ou 1 (presente).")

def registrar_frequencia_service(aula_id, aluno_id, presente, data_presenca):
    validar_presente_service(presente)
    frequencia_existente = verificar_frequencia_existente(aula_id, aluno_id)
    if frequencia_existente:
        raise Exception("Frequência já registrada para este aluno nesta aula.")
    
    inserir_frequencia_model(aula_id, aluno_id, presente, data_presenca)
    return {
        "mensagem": "Frequência registrada com sucesso"
    }

def atualizar_frequencia_service(id, aula_id, aluno_id, presente):
    validar_presente_service(presente)
    frequencia_existente = verificar_frequencia_existente(aula_id, aluno_id)
    if not frequencia_existente:
        raise Exception("Frequência não encontrada para este aluno nesta aula.")
    
    atualizar_frequencia(id, presente)
    return {
        "mensagem": "Frequência atualizada com sucesso"
    }
    
def deletar_frequencia_service(id):
    frequencia_existente = deletar_frequencia(id)
    if not frequencia_existente:
        raise Exception("Frequência não encontrada.")
    
    deletar_frequencia(id)
    return {
        "mensagem": "Frequência deletada com sucesso"
    }