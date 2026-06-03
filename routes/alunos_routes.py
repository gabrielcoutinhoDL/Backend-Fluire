from flask import Blueprint
from controllers.alunos_controller import *
from flask_jwt_extended import jwt_required

alunos_bp = Blueprint("alunos_bp", __name__)

@alunos_bp.route("/alunos", methods=["POST"])
@jwt_required()
def criar():
    return criar_aluno_controller()

@alunos_bp.route("/alunos", methods=["GET"])
@jwt_required()
def buscar_todos():
    return buscar_todos_alunos_controller()

@alunos_bp.route("/alunos/<int:id>", methods=["GET"])
@jwt_required()
def buscar_por_id(id):
    return buscar_aluno_por_id_controller(id)

@alunos_bp.route("/alunos/<int:id>", methods=["PUT"])
@jwt_required()
def atualizar(id):
    return atualizar_aluno_controller(id)

@alunos_bp.route("/alunos/<int:id>", methods=["DELETE"])
@jwt_required()
def deletar(id):
    return deletar_aluno_controller(id)

@alunos_bp.route("/alunos/nome/<string:nome>", methods=["GET"])
def buscar_por_nome(nome):
    return buscar_aluno_por_nome_controller(nome)