from flask import request, jsonify
from services.frequencias_service import *


# validar se o resultado da frequencias é 1 ou 0, caso seja 1, o aluno está presente, caso seja 0, o aluno está ausente
def listar_frequencias_controller():
    try:
        frequencias = todas_listar_frequencias_service()
        return jsonify(frequencias), 200

    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 400

def buscar_frequencias_aula_controller(aula_id):
    try:
        frequencias = buscar_frequencias_aula_service(aula_id)

        return jsonify(frequencias), 200

    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 400
        
def validar_presente(presente):
    if presente not in [0, 1]:
        raise Exception("Valor de 'presente' deve ser 0 (ausente) ou 1 (presente).")
        
def registrar_frequencias_controller():
    dados = request.json

    aula_id = dados.get("aula_id")
    aluno_id = dados.get("aluno_id")
    presente = dados.get("presente")

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

    validar_presente(presente)

    try:
        resultado = registrar_frequencias_service(aula_id, aluno_id, presente)
        return jsonify(resultado), 201
    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 400
    
       
def atualizar_frequencias_controller(id):
    dados = request.json

    aula_id = dados.get("aula_id")
    aluno_id = dados.get("aluno_id")
    presente = dados.get("presente")

    validar_presente(presente)
    try:
        resultado = atualizar_frequencias_service(id, aula_id, aluno_id, presente)
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 400
    
    
def deletar_frequencias_controller(id):
    try:
        resultado = deletar_frequencias_service(id)
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 400