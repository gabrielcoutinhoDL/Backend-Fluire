from config.database import get_connection

class DashboardService:
    def get_dashboard():
        try:
            total_alunos = DashboardService.get_total_alunos()
            total_aulas = DashboardService.get_total_aulas()
            media_frequencia = DashboardService.get_media_frequencia()
            proximas_aulas = DashboardService.get_proximas_aulas()
            total_alunos_com_falta = DashboardService.get_total_alunos_com_falta()

            dashboard_data = {
                "total_alunos": total_alunos,
                "total_aulas": total_aulas,
                "media_frequencia": media_frequencia,
                "proximas_aulas": proximas_aulas,
                "total_alunos_com_falta": total_alunos_com_falta
            }

            return dashboard_data
        except Exception as e:
            raise Exception(f"Erro ao obter dados do dashboard: {str(e)}")
    
    def get_proximas_aulas():
        try:
            connection = get_connection()
            cursor = connection.cursor()

            # Consulta para obter as próximas aulas
            cursor.execute("SELECT * FROM aulas WHERE data_hora > NOW() ORDER BY data_hora ASC LIMIT 5")
            proximas_aulas = cursor.fetchall()

            # Fechar a conexão com o banco de dados
            cursor.close()
            connection.close()

            return proximas_aulas
        except Exception as e:
            raise Exception(f"Erro ao obter próximas aulas: {str(e)}")


    def get_media_frequencia():
        try:
            connection = get_connection()
            cursor = connection.cursor()

            # Consulta para calcular a média de frequência dos alunos
            cursor.execute("SELECT AVG(CASE WHEN presente = TRUE THEN 1 ELSE 0 END) FROM aula_alunos")
            media_frequencia = cursor.fetchone()[0]

            # Fechar a conexão com o banco de dados
            cursor.close()
            connection.close()

            return media_frequencia
        except Exception as e:
            raise Exception(f"Erro ao calcular média de frequência: {str(e)}")


    def get_total_alunos():
        try:
            connection = get_connection()
            cursor = connection.cursor()

            # Consulta para obter o número total de alunos
            cursor.execute("SELECT COUNT(*) FROM alunos")
            total_alunos = cursor.fetchone()[0]

            # Fechar a conexão com o banco de dados
            cursor.close()
            connection.close()

            return total_alunos
        except Exception as e:
            raise Exception(f"Erro ao obter total de alunos: {str(e)}")
        
    
    def get_total_aulas():
        try:
            connection = get_connection()
            cursor = connection.cursor()

            # Consulta para obter o número total de aulas
            cursor.execute("SELECT COUNT(*) FROM aulas")
            total_aulas = cursor.fetchone()[0]

            # Fechar a conexão com o banco de dados
            cursor.close()
            connection.close()

            return total_aulas
        except Exception as e:
            raise Exception(f"Erro ao obter total de aulas: {str(e)}")
        
    
# Consulta para obter para total de alunos com falta
    def get_total_alunos_com_falta():
        try:
            connection = get_connection()
            cursor = connection.cursor()

            # Consulta para obter o número total de alunos com falta
            cursor.execute("SELECT COUNT(*) FROM aula_alunos WHERE presente = FALSE")
            total_associacoes = cursor.fetchone()[0]     

            # Fechar a conexão com o banco de dados
            cursor.close()
            connection.close()

            return total_associacoes
        except Exception as e:
            raise Exception(f"Erro ao obter total de alunos com falta: {str(e)}")