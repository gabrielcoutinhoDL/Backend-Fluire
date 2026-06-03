from flask import Blueprint
from controllers.aula_alunos_controller import *

aula_alunos_bp = Blueprint("aula_alunos_bp", __name__)

@aula_alunos_bp.route("/aula-alunos", methods=["POST"])
def associar_aluno_a_aula():
    return associar_aluno_a_aula_controller()

@aula_alunos_bp.route("/aula-alunos", methods=["DELETE"])
def remover_aluno_da_aula():
    return remover_aluno_da_aula_controller()