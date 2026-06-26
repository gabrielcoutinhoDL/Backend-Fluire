from config.database import get_connection


class AlunosModel:

    @staticmethod
    def buscar_todos_alunos():
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM alunos")
                return cursor.fetchall()
        finally:
            connection.close()

    @staticmethod
    def buscar_aluno_por_id(id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM alunos WHERE id = %s", (id,))
                return cursor.fetchone()
        finally:
            connection.close()

    @staticmethod
    def criar_aluno(nome, telefone=None, email=None, usuario_logado_id=None):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO alunos (nome, telefone, email, created_by) VALUES (%s, %s, %s, %s) RETURNING id",
                    (nome, telefone, email, usuario_logado_id)
                )
                aluno_id = cursor.fetchone()["id"]
                connection.commit()
                return aluno_id
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
                cursor.execute(
                    "UPDATE alunos SET nome = %s, telefone = %s, email = %s, updated_by = %s WHERE id = %s",
                    (nome, telefone, email, usuario_logado_id, id)
                )
                connection.commit()
                return cursor.rowcount > 0
        finally:
            connection.close()

    @staticmethod
    def deletar_aluno(id, usuario_logado_id=None):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM alunos WHERE id = %s", (id,))
                connection.commit()
                return cursor.rowcount > 0
        finally:
            connection.close()

    @staticmethod
    def buscar_alunos_por_nome(nome):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM alunos WHERE nome LIKE %s", (f'%{nome}%',))
                return cursor.fetchall()
        finally:
            connection.close()