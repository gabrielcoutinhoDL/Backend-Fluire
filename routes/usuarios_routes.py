from flask import Blueprint
from controllers.usuarios_controller import *

usuarios_bp = Blueprint ("usuarios_bd", __name__)

@usuarios_bp.route("/login", methods= ["POST"])
def login():
    return controller_usuario()