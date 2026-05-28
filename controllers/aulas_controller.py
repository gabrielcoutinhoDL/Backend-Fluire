from flask import request, jsonify
from models.aulas_model import *


def criar_aula_controller():
    dados = request.json

    nome = dados.get("nome")
    usuario_id = dados.get("usuario_id")
    horario_inicio = dados.get("horario_inicio")
    horario_fim = dados.get("horario_fim")
    frequencia = dados.get("frequencia")
    dia_semana = dados.get("dia_semana")

    # validações
    if not nome:
        return jsonify({
            "erro": "Nome obrigatório"
        }), 400

    if not usuario_id:
        return jsonify({
            "erro": "Usuário ID obrigatório"
        }), 400

    if not horario_inicio:
        return jsonify({
            "erro": "Horário de início obrigatório"
        }), 400

    if not horario_fim:
        return jsonify({
            "erro": "Horário de fim obrigatório"
        }), 400

    aula_id = AulasModel.criar_aula(nome, usuario_id, horario_inicio, horario_fim, frequencia, dia_semana)

    return jsonify({
        "mensagem": "Aula criada com sucesso",
        "id": aula_id
    }), 201
    
def buscar_todas_aulas_controller():
    aulas = AulasModel.buscar_todas_aulas()
    return jsonify(aulas), 200

def buscar_aula_por_id_controller(id):
    aula = AulasModel.buscar_aula_por_id(id)

    if not aula:
        return jsonify({
            "erro": "Aula não encontrada"
        }), 404

    return jsonify(aula), 200

def atualizar_aula_controller(id):
    dados = request.json

    nome = dados.get("nome")
    usuario_id = dados.get("usuario_id")
    horario_inicio = dados.get("horario_inicio")
    horario_fim = dados.get("horario_fim")
    frequencia = dados.get("frequencia")
    dia_semana = dados.get("dia_semana")

    aula_existente = AulasModel.buscar_aula_por_id(id)

    if not aula_existente:
        return jsonify({
            "erro": "Aula não encontrada"
        }), 404

    AulasModel.atualizar_aula(id, nome, usuario_id, horario_inicio, horario_fim, frequencia, dia_semana)

    return jsonify({
        "mensagem": "Aula atualizada com sucesso"
    }), 200
    
def deletar_aula_controller(id):
    aula_existente = AulasModel.buscar_aula_por_id(id)

    if not aula_existente:
        return jsonify({
            "erro": "Aula não encontrada"
        }), 404

    AulasModel.deletar_aula(id)

    return jsonify({
        "mensagem": "Aula deletada com sucesso"
    }), 200
    