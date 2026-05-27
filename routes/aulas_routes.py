from flask import Blueprint
from controllers.aulas_controller import *

aulas_bp = Blueprint("aulas_bp", __name__)

@aulas_bp.route("/aulas", methods=["POST"])
def criar():
    return criar_aula_controller()

@aulas_bp.route("/aulas", methods=["GET"])
def buscar_todas():
    return buscar_todas_aulas_controller()

@aulas_bp.route("/aulas/<int:id>", methods=["GET"])
def buscar_por_id(id):
    return buscar_aula_por_id_controller(id)

@aulas_bp.route("/aulas/<int:id>", methods=["PUT"])
def atualizar(id):
    return atualizar_aula_controller(id)

@aulas_bp.route("/aulas/<int:id>", methods=["DELETE"])
def deletar(id):
    return deletar_aula_controller(id)

