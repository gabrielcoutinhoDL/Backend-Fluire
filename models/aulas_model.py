from config.database import get_connection

class AulasModel:
    
    def criar_aula(nome, usuario_id, horario_inicio, horario_fim, frequencia=None, dia_semana=None):
        connection = get_connection()

        try:
            with connection.cursor() as cursor:

                # valida se usuário existe
                cursor.execute("SELECT id FROM usuarios WHERE id = %s", (usuario_id,))
                if not cursor.fetchone():
                    raise Exception("Usuário não encontrado")

                sql = """
                    INSERT INTO aulas 
                    (nome, usuario_id, horario_inicio, horario_fim, frequencia, dia_semana)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """

                cursor.execute(sql, (nome, usuario_id, horario_inicio, horario_fim, frequencia, dia_semana))
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
      
            
    def atualizar_aula(id, nome, usuario_id, horario_inicio, horario_fim, frequencia, dia_semana):
        connection = get_connection()
        
        try:
            with connection.cursor() as cursor:
                sql = """
                    UPDATE aulas 
                    SET nome = %s, usuario_id = %s, horario_inicio = %s, horario_fim = %s, frequencia = %s, dia_semana = %s
                    WHERE id = %s
                """
                cursor.execute(sql, (nome, usuario_id, horario_inicio, horario_fim, frequencia, dia_semana, id))
                if cursor.rowcount == 0:
                    raise Exception("Aula não encontrada")
                connection.commit()
                
                return cursor.rowcount  
            
        except Exception as e:
            connection.rollback()
            raise e
        
        finally:
            connection.close()
         
    
    def deletar_aula(id):
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
            
            