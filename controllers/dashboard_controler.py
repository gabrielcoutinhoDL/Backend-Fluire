from flask import jsonify

from services.dashboard_service import DashboardService


class DashboardController:

    @staticmethod
    def get_dashboard():

        try:

            data = DashboardService.get_dashboard()

            return jsonify({
                "success": True,
                "message": "Dashboard carregado com sucesso",
                "data": data
            }), 200

        except Exception as e:

            return jsonify({
                "success": False,
                "message": str(e)
            }), 500