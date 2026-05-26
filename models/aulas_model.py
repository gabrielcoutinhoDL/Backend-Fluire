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
                return result
        finally:
            connection.close()   
         
    def buscar_aula_por_id(id):
        connection = get_connection()
        
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM aulas WHERE id = %s"
                cursor.execute(sql, (id,))
                result = cursor.fetchone()
                return result
        finally:
            connection.close()
            
    def atualizar_aula(id, nome=None, usuario_id=None, horario_inicio=None, horario_fim=None, frequencia=None, dia_semana=None):
        connection = get_connection()
        
        try:
            with connection.cursor() as cursor:
                sql = """
                    UPDATE aulas 
                    SET nome = %s, usuario_id = %s, horario_inicio = %s, horario_fim = %s, frequencia = %s, dia_semana = %s 
                    WHERE id = %s
                """
                cursor.execute(sql, (nome, usuario_id, horario_inicio, horario_fim, frequencia, dia_semana, id))
                connection.commit()
                
                return print("Aula atualizada com sucesso! Linhas afetadas:", cursor.rowcount)

        finally:
            connection.close()        
    
    def deletar_aula(id):
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM aulas WHERE id = %s"
                cursor.execute(sql, (id,))
                connection.commit()
                
                return print("Aula deletada com sucesso! Linhas afetadas:", cursor.rowcount)

        finally:
            connection.close()
            
            