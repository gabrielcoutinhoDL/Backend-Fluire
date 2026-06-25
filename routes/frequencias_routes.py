from flask import Blueprint
from flask_jwt_extended import jwt_required

from controllers.frequencias_controller import *

frequencias_bp = Blueprint('frequencias', __name__)

@frequencias_bp.route('/frequencias', methods=['GET'])
def listar_frequencias():
    return listar_frequencias_controller() ##feito

@frequencias_bp.route('/frequencias/aulas/<int:aula_id>', methods=['GET'])
def buscar_frequencias_aula(aula_id):
    return buscar_frequencias_aula_controller(aula_id) #feito

@frequencias_bp.route('/frequencias', methods=['POST'])
@jwt_required()
def registrar_frequencias():
    return registrar_frequencias_controller() ##feito

@frequencias_bp.route('/frequencias/<int:id>', methods=['PUT'])
@jwt_required()
def atualizar_frequencias(id):
    return atualizar_frequencias_controller(id) ##feito

@frequencias_bp.route('/frequencias/<int:id>', methods=['DELETE'])
@jwt_required()
def deletar_frequencias(id):
    return deletar_frequencias_controller(id) #feito
