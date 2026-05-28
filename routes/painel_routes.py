from flask import Blueprint
from controllers.painel_controler import DashboardController


painel_bp =  Blueprint ('painel', __name__)

@painel_bp.route(
    '/painel',
    methods=['GET']
)
def painel():
    return DashboardController.get_dashboard()