from config.database import get_connection


class AlunosModel:
    
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
            
    def criar_aluno(nome, telefone=None, email=None):
        connection = get_connection()
    
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO alunos (nome, telefone, email) VALUES (%s, %s, %s)"
                cursor.execute(sql, (nome, telefone, email))
                connection.commit()
                
                return cursor.lastrowid

        finally:
            connection.close()
        
    def atualizar_aluno(id, nome=None, telefone=None, email=None):
        connection = get_connection()
        
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE alunos SET nome = %s, telefone = %s, email = %s WHERE id = %s"
                cursor.execute(sql, (nome, telefone, email, id))
                connection.commit()
                
                return print("Aluno atualizado com sucesso! Linhas afetadas:", cursor.rowcount)

        finally:
            connection.close()
            
    def deletar_aluno(id):
        connection = get_connection()
        
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM alunos WHERE id = %s"
                cursor.execute(sql, (id,))
                connection.commit()
                
                return print("Aluno deletado com sucesso! Linhas afetadas:", cursor.rowcount)

        finally:
            connection.close()

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
        