from flask import Blueprint
from controllers.alunos_controller import *

alunos_bp = Blueprint("alunos_bp", __name__)

@alunos_bp.route("/alunos", methods=["POST"])
def criar():
    return criar_aluno_controller()

@alunos_bp.route("/alunos", methods=["GET"])
def buscar_todos():
    return buscar_todos_alunos_controller()

@alunos_bp.route("/alunos/<int:id>", methods=["GET"])
def buscar_por_id(id):
    return buscar_aluno_por_id_controller(id)

@alunos_bp.route("/alunos/<int:id>", methods=["PUT"])
def atualizar(id):
    return atualizar_aluno_controller(id)

@alunos_bp.route("/alunos/<int:id>", methods=["DELETE"])
def deletar(id):
    return deletar_aluno_controller(id)

@alunos_bp.route("/alunos/nome/<string:nome>", methods=["GET"])
def buscar_por_nome(nome):
    return buscar_aluno_por_nome_controller(nome)