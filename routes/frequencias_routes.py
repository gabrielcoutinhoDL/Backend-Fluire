from flask import Blueprint

from controllers.frequencias_controller import *

frequencias_bp = Blueprint('frequencias', __name__)

@frequencias_bp.route('/frequencias', methods=['GET'])
def listar_frequencia():
    return listar_frequencia_controller()

@frequencias_bp.route('/frequencias/aula/<int:aula_id>', methods=['GET'])
def buscar_frequencias_aula(aula_id):
    return buscar_frequencias_aula_controller(aula_id)

@frequencias_bp.route('/frequencias', methods=['POST'])
def registrar_frequencia():
    return registrar_frequencia_controller()

@frequencias_bp.route('/frequencias/<int:id>', methods=['PUT'])
def atualizar_frequencia(id):
    return atualizar_frequencia_controller(id)
        
@frequencias_bp.route('/frequencias/<int:id>', methods=['DELETE'])
def deletar_frequencia(id):
    return deletar_frequencia_controller(id)
