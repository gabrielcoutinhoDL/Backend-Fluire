from flask import Blueprint
from controllers.usuarios_controller import *

usuarios_bp = Blueprint ("usuarios_bd", __name__)

@usuarios_bp.route("/login", methods=["POST"])
def login_usuario():
    return login_usuario_controller()

@usuarios_bp.route("/usuarios", methods=["POST"])
def criar_usuario():
    return criar_usuario_controller()

@usuarios_bp.route("/usuarios/<string:nome>", methods=["GET"])
def buscar_usuario_nome(nome):
    return buscar_usuario_nome_controller(nome)

@usuarios_bp.route("/usuarios/<int:id>", methods=["PUT"])
def atualizar_usuario(id):
    return atualizar_usuario_controller(id)

@usuarios_bp.route("/usuarios/<int:id>", methods=["DELETE"])
def deletar_usuario(id):
    return deletar_usuario_controller(id)

@usuarios_bp.route("/recuperar-senha", methods=["POST"])
def recuperar_senha():
    return recuperar_senha_controller()