from flask import request, jsonify
from models.alunos_model import *


def criar_aluno_controller():
    dados = request.json

    nome = dados.get("nome")
    email = dados.get("email")
    telefone = dados.get("telefone")

    # validações
    if not nome:
        return jsonify({
            "erro": "Nome obrigatório"
        }), 400

    if not telefone:
        return jsonify({
            "erro": "Telefone obrigatório"
        }), 400

    if not email:
        return jsonify({
            "erro": "Email obrigatório"
        }), 400

    aluno_id = AlunosModel.criar_aluno(nome, telefone, email)

    return jsonify({
        "mensagem": "Aluno criado com sucesso",
        "id": aluno_id
    }), 201


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

    aluno_existente = AlunosModel.buscar_aluno_por_id(id)

    if not aluno_existente:
        return jsonify({
            "erro": "Aluno não encontrado"
        }), 404

    AlunosModel.atualizar_aluno(id, nome, telefone, email)

    return jsonify({
        "mensagem": "Aluno atualizado com sucesso"
    }), 200
    
    
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
    alunos = AlunosModel.buscar_aluno_por_nome(nome)

    if not alunos:
        return jsonify({
            "erro": "Nenhum aluno encontrado com esse nome"
        }), 404

    return jsonify(alunos), 200

