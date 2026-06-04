from flask import Blueprint
from controllers.aula_alunos_controller import *

aula_alunos_bp = Blueprint("aula_alunos_bp", __name__)

@aula_alunos_bp.route("/aula-alunos", methods=["POST"])
def associar_aluno_a_aula():
    return associar_aluno_a_aula_controller()

@aula_alunos_bp.route("/aula-alunos", methods=["DELETE"])
def remover_aluno_da_aula():
    return remover_aluno_da_aula_controller()

@aula_alunos_bp.route("/aula-alunos", methods=["GET"])
def listar_aula_alunos():
    return listar_aula_alunos_controller()

@aula_alunos_bp.route("/aula-alunos/<int:id>", methods=["GET"])
def buscar_aula_aluno_por_id(id):
    return buscar_aula_aluno_por_id_controller(id)

@aula_alunos_bp.route("/aulas/<int:aula_id>/alunos", methods=["GET"])
def obter_alunos_por_aula(aula_id):
    return obter_alunos_por_aula_controller(aula_id)

@aula_alunos_bp.route("/alunos/<int:aluno_id>/aulas", methods=["GET"])
def obter_aulas_por_aluno(aluno_id):
    return obter_aulas_por_aluno_controller(aluno_id)