from flask import request, jsonify
from models.alunos_model import *
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
import os


def criar_aluno_controller():
    dados = request.json

    nome = dados.get("nome")
    email = dados.get("email")
    telefone = dados.get("telefone")
    usuario_logado_id = get_jwt_identity()


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
    usuario_logado_id = dados.get("usuario_logado_id")
    aluno_existente = AlunosModel.buscar_aluno_por_id(id)

    if not aluno_existente:
        return jsonify({
            "erro": "Aluno não encontrado"
        }), 404

    AlunosModel.atualizar_aluno(id, nome, telefone, email, usuario_logado_id)

    return jsonify({
        "mensagem": "Aluno atualizado com sucesso"
    }), 200
    

def deletar_aluno_controller(id):
    dados = request.json
    usuario_logado_id = dados.get("usuario_logado_id")
    aluno_existente = AlunosModel.buscar_aluno_por_id(id)

    if not aluno_existente:
        return jsonify({
            "erro": "Aluno não encontrado"
        }), 404

    AlunosModel.deletar_aluno(id, usuario_logado_id)

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




