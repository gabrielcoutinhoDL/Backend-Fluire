from config.database import get_connection
from datetime import datetime


class DashboardService:
    @staticmethod
    def get_dashboard():
        try:
            total_alunos = DashboardService.get_total_alunos()
            total_aulas = DashboardService.get_total_aulas()
            media_frequencias = DashboardService.get_media_frequencias()
            proximas_aulas = DashboardService.get_proximas_aulas()
            total_alunos_com_falta = DashboardService.get_total_alunos_com_falta()

            dashboard_data = {
                "success": True,
                "data": {
                    "alunos_presentes": total_alunos,
                    "aulas_hoje": len(proximas_aulas),
                    "em_andamento": min(len(proximas_aulas), 1),
                    "frequencias_media": media_frequencias,
                    "semana_frequencias": DashboardService.get_semana_frequencias(),
                    "today_classes": proximas_aulas,
                    "total_alunos": total_alunos,
                    "total_aulas": total_aulas,
                    "total_alunos_com_falta": total_alunos_com_falta,
                }
            }

            return dashboard_data
        except Exception as e:
            raise Exception(f"Erro ao obter dados do dashboard: {str(e)}")

    @staticmethod
    def get_proximas_aulas():
        try:
            connection = get_connection()
            cursor = connection.cursor()

            dia_semana = datetime.now().isoweekday()
            cursor.execute(
                "SELECT * FROM aulas WHERE dia_semana = %s ORDER BY horario_inicio ASC LIMIT 5",
                (dia_semana,),
            )
            aulas = cursor.fetchall()

            cursor.close()
            connection.close()

            resultado = []
            for aula in aulas:
                resultado.append({
                    "title": aula.get("nome", "Aula"),
                    "teacher": f"Professor #{aula.get('usuario_id', '')}",
                    "time": f"{aula.get('horario_inicio', '')} - {aula.get('horario_fim', '')}",
                    "students": "0 alunos",
                    "status": "ativa",
                })

            return resultado
        except Exception as e:
            raise Exception(f"Erro ao obter próximas aulas: {str(e)}")

    @staticmethod
    def get_media_frequencias():
        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                "SELECT AVG(CASE WHEN presente = 1 THEN 1 ELSE 0 END) FROM frequencias"
            )
            row = cursor.fetchone()
            media_frequencias = list(row.values())[0] if row else 0

            cursor.close()
            connection.close()

            if media_frequencias is None:
                return 0
            return round(float(media_frequencias) * 100)
        except Exception:
            return 0

    def get_semana_frequencias():
        dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute(
                """
                SELECT DAYOFWEEK(data_presenca) as dia, COUNT(*) as total
                FROM frequencias
                WHERE presente = 1
                GROUP BY DAYOFWEEK(data_presenca)
                """
            )
            rows = cursor.fetchall()
            cursor.close()
            connection.close()

            contagem = {i: 0 for i in range(1, 8)}
            for row in rows:
                contagem[row.get('dia', 0)] = row.get('total', 0)

            max_valor = max(contagem.values()) if contagem.values() else 0
            resultado = []
            for i, nome in enumerate(dias, start=1):
                valor = contagem.get(i, 0)
                altura = 20.0 if max_valor == 0 else (valor / max_valor) * 80 + 20
                resultado.append({"day": nome, "value": altura})
            return resultado
        except Exception:
            return [{"day": d, "value": 20.0} for d in dias]

    @staticmethod
    def get_total_alunos():
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) as total FROM alunos")
            row = cursor.fetchone()
            cursor.close()
            connection.close()
            return row.get('total', 0) if row else 0
        except Exception as e:
            raise Exception(f"Erro ao obter total de alunos: {str(e)}")

    @staticmethod
    def get_total_aulas():
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) as total FROM aulas")
            row = cursor.fetchone()
            cursor.close()
            connection.close()
            return row.get('total', 0) if row else 0
        except Exception as e:
            raise Exception(f"Erro ao obter total de aulas: {str(e)}")

    @staticmethod
    def get_total_alunos_com_falta():
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) as total FROM frequencias WHERE presente = 0")
            row = cursor.fetchone()
            cursor.close()
            connection.close()
            return row.get('total', 0) if row else 0
        except Exception as e:
            raise Exception(f"Erro ao obter total de alunos com falta: {str(e)}")
