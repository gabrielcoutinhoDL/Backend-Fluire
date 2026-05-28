from models.frequencias_model import (
    buscar_todas_frequencias,
    buscar_frequencias_por_aula,
    verificar_frequencia_existente,
    inserir_frequencia,
    atualizar_frequencia,
    deletar_frequencia,
)


def listar_frequencias_service():
    return buscar_todas_frequencias()


def buscar_frequencias_aula_service(aula_id):
    return buscar_frequencias_por_aula(aula_id)


def registrar_frequencia_service(aula_id, aluno_id, presente, data_presenca):
    frequencia_existente = verificar_frequencia_existente(
        aula_id,
        aluno_id,
        data_presenca,
    )

    if frequencia_existente:
        atualizar_frequencia(frequencia_existente["id"], presente)
        return {
            "sucesso": True,
            "mensagem": "Frequência atualizada com sucesso",
        }

    inserir_frequencia(aula_id, aluno_id, presente, data_presenca)
    return {
        "sucesso": True,
        "mensagem": "Frequência registrada com sucesso",
    }


def atualizar_frequencia_service(id, presente):
    atualizar_frequencia(id, presente)
    return {
        "sucesso": True,
        "mensagem": "Frequência atualizada com sucesso",
    }


def deletar_frequencia_service(id):
    deletar_frequencia(id)
    return {
        "sucesso": True,
        "mensagem": "Frequência removida com sucesso",
    }
