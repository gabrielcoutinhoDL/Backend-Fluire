from flask import Blueprint

from controllers.frequencias_controller import (
    listar_frequencia,
    buscar_frequencias_aula,
    registrar_frequencia,
    atualizar_frequencia,
    deletar_frequencia,
)

frequencia_bp = Blueprint(
    "frequencia_bp",
    __name__,
    url_prefix="/frequencias",
)


@frequencia_bp.route("/", methods=["GET"])
def route_listar_frequencia():
    return listar_frequencia()


@frequencia_bp.route("/aula/<int:aula_id>", methods=["GET"])
def route_buscar_frequencias_aula(aula_id):
    return buscar_frequencias_aula(aula_id)


@frequencia_bp.route("/", methods=["POST"])
def route_registrar_frequencia():
    return registrar_frequencia()


@frequencia_bp.route("/<int:id>", methods=["PUT"])
def route_atualizar_frequencia(id):
    return atualizar_frequencia(id)


@frequencia_bp.route("/<int:id>", methods=["DELETE"])
def route_deletar_frequencia(id):
    return deletar_frequencia(id)
