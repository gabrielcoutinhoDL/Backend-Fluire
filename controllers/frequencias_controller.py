from flask import request, jsonify
from services.frequencia_service import *


# validar se o resultado da frequencia é 1 ou 0, caso seja 1, o aluno está presente, caso seja 0, o aluno está ausente
def listar_frequencia():
    try:
        frequencias = todas_listar_frequencias_service()
        return jsonify(frequencias), 200
    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 400

def buscar_frequencias_aula(aula_id):
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
        
def registrar_frequencia():
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
        resultado = registrar_frequencia_service(aula_id, aluno_id, presente, data_presenca)
        return jsonify(resultado), 201
    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 400
    
       
def atualizar_frequencia(id, aula_id, aluno_id, presente, data_presenca):
    validar_presente(presente)
    try:
        resultado = atualizar_frequencia_service(id, aula_id, aluno_id, presente, data_presenca)
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 400
    
    
def deletar_frequencia(id):
    try:
        resultado = deletar_frequencia_service(id)
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 400