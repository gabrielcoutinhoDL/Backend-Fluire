
from flask import request, jsonify
from models.aulas_model import *
from flask_jwt_extended import jwt_required, get_jwt_identity

@jwt_required()

def criar_aula_controller():
    dados = request.json

    nome = dados.get("nome")
    usuario_id = dados.get("usuario_id")
    horario_inicio = dados.get("horario_inicio")
    horario_fim = dados.get("horario_fim")
    frequencia = dados.get("frequencia")
    dia_semana = dados.get("dia_semana")
    usuario_logado_id = int(get_jwt_identity())

    if not nome:
        return jsonify({
            "erro": "Nome obrigatório"
        }), 400

    if not usuario_id:
        return jsonify({
            "erro": "ID do usuário obrigatório"
        }), 400

    if not horario_inicio:
        return jsonify({
            "erro": "Horário de início obrigatório"
        }), 400

    if not horario_fim:
        return jsonify({
            "erro": "Horário de fim obrigatório"
        }), 400

    if not frequencia:
        return jsonify({
            "erro": "Frequência obrigatória"
        }), 400

    if not dia_semana:
        return jsonify({
            "erro": "Dia da semana obrigatório"
        }), 400

    try:
        aula_id = AulasModel.criar_aula(nome, usuario_id, horario_inicio, horario_fim, frequencia, dia_semana, usuario_logado_id)
        return jsonify({
            "id": aula_id
        }), 201
    except Exception as e:
        return jsonify({
            "erro": f"Erro ao criar aula: {str(e)}"
        }), 500


def buscar_todas_aulas_controller():
    try:
        aulas = AulasModel.buscar_todas_aulas()

        return jsonify(aulas), 200

    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 500

@jwt_required()
def atualizar_aula_controller(id):
    dados = request.json

    nome = dados.get("nome")
    usuario_id = dados.get("usuario_id")
    horario_inicio = dados.get("horario_inicio")
    horario_fim = dados.get("horario_fim")
    frequencia = dados.get("frequencia")
    dia_semana = dados.get("dia_semana")
    usuario_logado_id = get_jwt_identity()

    aula_existente = AulasModel.buscar_aula_por_id(id)

    if not aula_existente:
        return jsonify({
            "erro": "Aula não encontrada"
        }), 404

    AulasModel.atualizar_aula(id, nome, usuario_id, horario_inicio, horario_fim, frequencia, dia_semana, usuario_logado_id)

    return jsonify({
        "mensagem": "Aula atualizada com sucesso"
    }), 200
    
    
def deletar_aula_controller(id):
    try:
        AulasModel.deletar_aula(id)
        return jsonify({
            "mensagem": "Aula deletada com sucesso"
        }), 200
    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 500
    
