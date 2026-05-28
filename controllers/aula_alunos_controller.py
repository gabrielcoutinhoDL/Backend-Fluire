from flask import request, jsonify
from models.aula_alunos_model import *

def associar_aluno_a_aula_controller():
    dados = request.json

    aula_id = dados.get("aula_id")
    aluno_id = dados.get("aluno_id")

    if not aula_id:
        return jsonify({
            "erro": "Aula ID obrigatório"
        }), 400

    if not aluno_id:
        return jsonify({
            "erro": "Aluno ID obrigatório"
        }), 400

    try:
        AulaAlunosModel.associar_aluno_a_aula(aula_id, aluno_id)
        return jsonify({
            "mensagem": "Aluno associado à aula com sucesso"
        }), 201
    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 400
        
        
def buscar_aulas_por_aluno_id_controller(aluno_id):
    try:
        aulas = AulaAlunosModel.buscar_aulas_por_aluno_id(aluno_id)
        return jsonify(aulas), 200
    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 400


def remover_aluno_da_aula_controller():
    dados = request.json

    aula_id = dados.get("aula_id")
    aluno_id = dados.get("aluno_id")

    if not aula_id:
        return jsonify({
            "erro": "Aula ID obrigatório"
        }), 400

    if not aluno_id:
        return jsonify({
            "erro": "Aluno ID obrigatório"
        }), 400

    try:
        AulaAlunosModel.remover_aluno_da_aula(aula_id, aluno_id)
        return jsonify({
            "mensagem": "Aluno removido da aula com sucesso"
        }), 200
    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 400