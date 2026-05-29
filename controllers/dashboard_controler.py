from flask import jsonify
from services.dashboard_service import *

def get_dashboard_controller():
    try:
        dashboard_data = DashboardService.get_dashboard()
        return jsonify(dashboard_data), 200
    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 400