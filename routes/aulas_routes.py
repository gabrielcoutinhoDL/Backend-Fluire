from flask import Blueprint
from flask_jwt_extended import jwt_required
from controllers.aulas_controller import *

aulas_bp = Blueprint("aulas_bp", __name__)

@aulas_bp.route("/aulas", methods=["POST"])
@jwt_required()
def criar_aula():
    return criar_aula_controller()

@aulas_bp.route("/aulas", methods=["GET"])
def buscar_todas_aulas():
    return buscar_todas_aulas_controller()

@aulas_bp.route("/aulas/<int:id>", methods=["GET"])
def buscar_aula_por_id(id):
    return buscar_aula_por_id_controller(id)

@aulas_bp.route("/aulas/<int:id>", methods=["PUT"])
@jwt_required()
def atualizar(id):
    return atualizar_aula_controller(id)

@aulas_bp.route("/aulas/<int:id>", methods=["DELETE"])
@jwt_required()
def deletar(id):
    return deletar_aula_controller(id)

