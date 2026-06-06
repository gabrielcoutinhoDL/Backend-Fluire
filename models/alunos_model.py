from config.database import get_connection


class AlunosModel:
    
    @staticmethod
    def buscar_todos_alunos():
        connection = get_connection()
        
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM alunos"
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        finally:
            connection.close()

    @staticmethod
    def buscar_aluno_por_id(id):
        connection = get_connection()
        
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM alunos WHERE id = %s"
                cursor.execute(sql, (id,))
                result = cursor.fetchone()
                return result
        finally:
            connection.close()       
            
    @staticmethod
    def criar_aluno(nome, telefone=None, email=None, usuario_logado_id=None):
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                sql = """
                    INSERT INTO alunos (nome, telefone, email, created_by)
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(sql, (nome, telefone, email, usuario_logado_id))
                connection.commit()

                return cursor.lastrowid

        except Exception:
            connection.rollback()
            raise

        finally:
            connection.close()
        
    @staticmethod
    def atualizar_aluno(id, nome=None, telefone=None, email=None, usuario_logado_id=None):
        connection = get_connection()
        
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE alunos SET nome = %s, telefone = %s, email = %s, updated_by = %s WHERE id = %s"
                cursor.execute(sql, (nome, telefone, email, usuario_logado_id, id))
                connection.commit()
                
                return print("Aluno atualizado com sucesso! Linhas afetadas:", cursor.rowcount)
        finally:
            connection.close()
            
    @staticmethod
    def deletar_aluno(id, usuario_logado_id=None):
        connection = get_connection()
        
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM alunos WHERE id = %s"
                cursor.execute(sql, (id,))
                connection.commit()
                return cursor.rowcount > 0

        finally:
            connection.close()

    @staticmethod
    def buscar_alunos_por_nome(nome):
        connection = get_connection()
        
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM alunos WHERE nome LIKE %s"
                cursor.execute(sql, ('%' + nome + '%',))
                result = cursor.fetchall()
                return result
        finally:
            connection.close()
        