from flask import request, jsonify
from models.alunos_model import *
from flask_jwt_extended import jwt_required, get_jwt_identity

@jwt_required()

def criar_aluno_controller():
    dados = request.json
    nome = dados.get("nome")
    email = dados.get("email")
    telefone = dados.get("telefone")
    usuario_logado_id = dados.get("usuario_logado_id")

    if not nome:
        return jsonify({"erro": "Nome obrigatório"}), 400

    try:
        aluno_id = AlunosModel.criar_aluno(nome, telefone, email, usuario_logado_id)
        return jsonify({"id": aluno_id}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

    if not nome:
        return jsonify({"erro": "Nome obrigatório"}), 400

    if not email:
        return jsonify({"erro": "Email obrigatório"}), 400

    if not telefone:
        return jsonify({"erro": "Telefone obrigatório"}), 400

    try:
        aluno_id = AlunosModel.criar_aluno(nome, telefone, email, usuario_logado_id)
        return jsonify({"id": aluno_id}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 400


def buscar_todos_alunos_controller():
    alunos = AlunosModel.buscar_todos_alunos()
    return jsonify(alunos), 200


def buscar_aluno_por_id_controller(id):
    aluno = AlunosModel.buscar_aluno_por_id(id)

    if not aluno:
        return jsonify({
            "erro": "Aluno não encontrado"
        }), 404

    return jsonify(aluno), 200


def atualizar_aluno_controller(id):
    dados = request.json
    nome = dados.get("nome")
    email = dados.get("email")
    telefone = dados.get("telefone")
    usuario_logado_id = get_jwt_identity()
    
    if not nome:
        return jsonify({
            "erro": "Nome obrigatório"
        }), 400
        
    if not email:
        return jsonify({
            "erro": "Email obrigatório"
        }), 400
        
    if not telefone:
        return jsonify({
            "erro": "Telefone obrigatório"
        }), 400  
               
    try:    
             
        sucesso = AlunosModel.atualizar_aluno(id, nome, telefone, email, usuario_logado_id)
        if sucesso:
            return jsonify({
                "mensagem": "Aluno atualizado com sucesso"
            }), 200
        else:
            return jsonify({
                "erro": "Aluno não encontrado"
            }), 404
    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 400


def deletar_aluno_controller(id):
    aluno_existente = AlunosModel.buscar_aluno_por_id(id)

    if not aluno_existente:
        return jsonify({
            "erro": "Aluno não encontrado"
        }), 404

    AlunosModel.deletar_aluno(id)

    return jsonify({
        "mensagem": "Aluno deletado com sucesso"
    }), 200


def buscar_aluno_por_nome_controller(nome):
    alunos = AlunosModel.buscar_alunos_por_nome(nome)

    if not alunos:
        return jsonify({
            "erro": "Nenhum aluno encontrado com esse nome"
        }), 404

    return jsonify(alunos), 200
