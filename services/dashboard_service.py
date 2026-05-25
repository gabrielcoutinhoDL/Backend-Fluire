from config.database import get_connection

class DashboardService:
    
    @staticmethod
    def get_dashboard():
        
        ConnectDB = get_connection()
        
        try:
            
            with ConnectDB.cursor() as cursor:
                
                #total presença
                cursor.execute("SELECT COUNT(*) AS total FROM frequencias WHERE presentes = 1 AND DATE(data_presenca) = CURDATE()")
                alunos_presentes = cursor.fetchone()["total"]
                
                #total aulas
                cursor.execute ("SELECT COUNT(*) AS total FROM aulas")
                aulas_hoje = cursor.fetchone()["total"]
                
                #freq. média
                cursor.execute ("SELECT SUM(presencas) AS presencas, SUM(faltas) AS faltas FROM alunos")
                dados = cursor.fetchone()
                
                total_presencas = dados["presencas"] or 0
                total_faltas = dados["faltas"] or 0
                
                total = total_presencas + total_faltas 
                
                frequencia_media = 0
                
                if total > 0:
                    frequencia_media = round(
                        (total_presencas / total) * 100
                    )
                
                #lista aulas
                
                cursor.execute("""
                    SELECT
                        id,
                        nome,
                        usuario_id,
                        horario_inicio,
                        horario_fim,
                        frequencia
                    FROM aulas
                """)
                
                aulas = cursor.fetchall()
                
                return {
                    "alunos_presentes": alunos_presentes,
                    "aulas_hoje": aulas_hoje,                    
                    "em_andamento": 0,
                    "frequencia_media": frequencia_media,
                    "today_classes": [
                        
                        {
                            "id": aula["id"],
                            "title": aula["nome"],
                            "teacher": f"Professor #{aula['usuario_id']}",
                            "time": f"{aula['horario_inicio']} - {aula['horario_fim']}",
                            "students": str(aula["frequencia"]),
                            "status": "ativa"
                        }
                        
                        for aula in aulas
                    ]
                }
                
        finally:
            ConnectDB.close()