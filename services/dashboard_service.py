from config.database import get_connection
from datetime import datetime


class DashboardService:

    @staticmethod
    def get_dashboard():
        try:
            proximas_aulas = DashboardService.get_proximas_aulas()
            return {
                "success": True,
                "data": {
                    "alunos_presentes": DashboardService.get_total_alunos(),
                    "aulas_hoje": len(proximas_aulas),
                    "em_andamento": min(len(proximas_aulas), 1),
                    "frequencias_media": DashboardService.get_media_frequencias(),
                    "semana_frequencias": DashboardService.get_semana_frequencias(),
                    "today_classes": proximas_aulas,
                    "total_alunos": DashboardService.get_total_alunos(),
                    "total_aulas": DashboardService.get_total_aulas(),
                    "total_alunos_com_falta": DashboardService.get_total_alunos_com_falta(),
                }
            }
        except Exception as e:
            raise Exception(f"Erro ao obter dados do dashboard: {str(e)}")

    @staticmethod
    def get_proximas_aulas():
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                # dia_semana é VARCHAR no banco — converte para string
                dia_semana = str(datetime.now().isoweekday())
                cursor.execute(
                    "SELECT * FROM aulas WHERE dia_semana = %s ORDER BY horario_inicio ASC LIMIT 5",
                    (dia_semana,)
                )
                return [
                    {
                        "title": aula.get("nome", "Aula"),
                        "teacher": f"Professor #{aula.get('usuario_id', '')}",
                        "time": f"{aula.get('horario_inicio', '')} - {aula.get('horario_fim', '')}",
                        "students": "0 alunos",
                        "status": "ativa",
                    }
                    for aula in cursor.fetchall()
                ]
        finally:
            connection.close()

    @staticmethod
    def get_media_frequencias():
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT AVG(CASE WHEN presente = TRUE THEN 1 ELSE 0 END) FROM frequencias")
                row = cursor.fetchone()
                media = list(row.values())[0] if row else None
                return round(float(media) * 100) if media else 0
        except Exception:
            return 0
        finally:
            connection.close()

    def get_semana_frequencias():
        dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                # EXTRACT(DOW) retorna 0=Dom..6=Sáb; +1 equivale ao DAYOFWEEK do MySQL (1=Dom..7=Sáb)
                cursor.execute("""
                    SELECT (EXTRACT(DOW FROM data_presenca)::int + 1) as dia, COUNT(*) as total
                    FROM frequencias
                    WHERE presente = TRUE
                    GROUP BY EXTRACT(DOW FROM data_presenca)::int
                """)
                contagem = {i: 0 for i in range(1, 8)}
                for row in cursor.fetchall():
                    contagem[row.get('dia', 0)] = row.get('total', 0)

                max_valor = max(contagem.values()) or 1
                return [
                    {"day": nome, "value": (contagem.get(i, 0) / max_valor) * 80 + 20}
                    for i, nome in enumerate(dias, start=1)
                ]
        except Exception:
            return [{"day": d, "value": 20.0} for d in dias]
        finally:
            connection.close()

    @staticmethod
    def get_total_alunos():
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) as total FROM alunos")
                row = cursor.fetchone()
                return row.get('total', 0) if row else 0
        finally:
            connection.close()

    @staticmethod
    def get_total_aulas():
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) as total FROM aulas")
                row = cursor.fetchone()
                return row.get('total', 0) if row else 0
        finally:
            connection.close()

    @staticmethod
    def get_total_alunos_com_falta():
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) as total FROM frequencias WHERE presente = FALSE")
                row = cursor.fetchone()
                return row.get('total', 0) if row else 0
        finally:
            connection.close()
