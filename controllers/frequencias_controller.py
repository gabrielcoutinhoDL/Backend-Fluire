from flask import request, jsonify

from services.frequencia_service import (
    listar_frequencias_service,
    buscar_frequencias_aula_service,
    registrar_frequencia_service,
    atualizar_frequencia_service,
    deletar_frequencia_service,
)


def listar_frequencia():
    frequencias = listar_frequencias_service()
    return jsonify(frequencias), 200


def buscar_frequencias_aula(aula_id):
    frequencias = buscar_frequencias_aula_service(aula_id)
    return jsonify(frequencias), 200


def registrar_frequencia():
    data = request.get_json() or {}

    aula_id = data.get("aula_id")
    aluno_id = data.get("aluno_id")
    presente = data.get("presente")
    data_presenca = data.get("data_presenca")

    if not aula_id or not aluno_id:
        return jsonify({
            "sucesso": False,
            "mensagem": "Aula e aluno são obrigatórios",
        }), 400

    response = registrar_frequencia_service(
        aula_id,
        aluno_id,
        presente,
        data_presenca,
    )
    return jsonify(response), 201


def atualizar_frequencia(id):
    data = request.get_json() or {}
    presente = data.get("presente")

    response = atualizar_frequencia_service(id, presente)
    return jsonify(response), 200


def deletar_frequencia(id):
    response = deletar_frequencia_service(id)
    return jsonify(response), 200
