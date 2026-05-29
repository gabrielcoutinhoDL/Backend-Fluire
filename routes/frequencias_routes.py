from flask import Blueprint

from controllers.frequencias_controller import *

frequencias_bp = Blueprint('frequencias', __name__)

@frequencias_bp.route('/frequencias', methods=['GET'])
def listar_frequencia():
    return listar_frequencia()

@frequencias_bp.route('/frequencias/aula/<int:aula_id>', methods=['GET'])
def buscar_frequencias_aula(aula_id):
    return buscar_frequencias_aula(aula_id)

@frequencias_bp.route('/frequencias', methods=['POST'])
def registrar_frequencia():
    return registrar_frequencia()

@frequencias_bp.route('/frequencias/<int:id>', methods=['PUT'])
def atualizar_frequencia(id):
    dados = request.json

    aula_id = dados.get("aula_id")
    aluno_id = dados.get("aluno_id")
    presente = dados.get("presente")
    data_presenca = dados.get("data_presenca")

    if not aula_id:
        return jsonify({
            "erro": "Aula ID obrigatório"
        }), 400

    if not aluno_id:
        return jsonify({
            "erro": "Aluno ID obrigatório"
        }), 400

    if presente is None:
        return jsonify({
            "erro": "Presente obrigatório"
        }), 400

    if not data_presenca:
        return jsonify({
            "erro": "Data de presença obrigatória"
        }), 400

    validar_presente(presente)

    try:
        resultado = atualizar_frequencia_service(id, aula_id, aluno_id, presente)
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 400
        
@frequencias_bp.route('/frequencias/<int:id>', methods=['DELETE'])
def deletar_frequencia(id):
    try:
        resultado = deletar_frequencia_service(id)
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 400