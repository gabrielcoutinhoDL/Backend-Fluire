from config.database import get_connection
from flask import request, jsonify

class AulasModel:
                
    def criar_aula(nome, usuario_id, horario_inicio, horario_fim, frequencia, dia_semana, usuario_logado_id=None):
        connection = get_connection()
        
        try:
            with connection.cursor() as cursor:
                sql = """
                    INSERT INTO aulas (nome, usuario_id, horario_inicio, horario_fim, frequencia, dia_semana, created_by) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (nome, usuario_id, horario_inicio, horario_fim, frequencia, dia_semana, usuario_logado_id))
                connection.commit()
                return cursor.lastrowid
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            connection.close()
        
            
    def buscar_todas_aulas():
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM aulas"
                cursor.execute(sql)
                result = cursor.fetchall()

                # Converte resultados para dicionário
                aulas = []
                for row in result:
                    aulas.append({
                        'id': row[0],
                        'nome': row[1],
                        'usuario_id': row[2],
                        'horario_inicio': row[3],
                        'horario_fim': row[4],
                        'frequencia': row[5] if row[5] else None,
                        'dia_semana': row[6] if row[6] else None
                    })
                return aulas
        finally:
            connection.close()   
         
            
    def buscar_aula_por_id(id):
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM aulas WHERE id = %s"
                cursor.execute(sql, (id,))
                result = cursor.fetchone()

                if result:
                    return {
                        'id': result[0],
                        'nome': result[1],
                        'usuario_id': result[2],
                        'horario_inicio': result[3],
                        'horario_fim': result[4],
                        'frequencia': result[5] if result[5] else None,
                        'dia_semana': result[6] if result[6] else None
                    }
                return None
        finally:
            connection.close() 
            
          
    def atualizar_aula(id, nome, usuario_id, horario_inicio, horario_fim, frequencia, dia_semana, usuario_logado_id=None):
        connection = get_connection()
        
        try:
            with connection.cursor() as cursor:
                sql = """
                    UPDATE aulas 
                    SET nome = %s, usuario_id = %s, horario_inicio = %s, horario_fim = %s, frequencia = %s, dia_semana = %s, updated_by = %s
                    WHERE id = %s
                """
                cursor.execute(sql, (nome, usuario_id, horario_inicio, horario_fim, frequencia, dia_semana, usuario_logado_id, id))
                if cursor.rowcount == 0:
                    raise Exception("Aula não encontrada")
                connection.commit()
                
                return cursor.rowcount  
            
        except Exception as e:
            connection.rollback()
            raise e
        
        finally:
            connection.close()

           
    def deletar_aula(id, usuario_logado_id=None):
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM aulas WHERE id = %s"
                cursor.execute(sql, (id,))
                if cursor.rowcount == 0:
                    raise Exception("Aula não encontrada")
                
                connection.commit()
                
                return cursor.rowcount

        except Exception as e:
            connection.rollback()
            raise e

        finally:
            connection.close()
