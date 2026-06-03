from flask import Blueprint
from controllers.dashboard_controler import *

dashboard_bp = Blueprint('dashboard_bp', __name__)

@dashboard_bp.route('/painel', methods=['GET'])
def get_painel():
    return get_dashboard_controller()

@dashboard_bp.route('/dashboard', methods=['GET'])
def get_dashboard():
    return get_dashboard_controller()
