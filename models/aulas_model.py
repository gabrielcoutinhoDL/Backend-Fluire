from config.database import get_connection


class AulasModel:

    def criar_aula(nome, usuario_id, horario_inicio, horario_fim, frequencia=None, dia_semana=None, usuario_logado_id=None):
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id FROM usuarios WHERE id = %s", (usuario_id,))
                if not cursor.fetchone():
                    raise Exception("Usuário não encontrado")

                sql = """
                    INSERT INTO aulas 
                    (nome, usuario_id, horario_inicio, horario_fim, frequencia, dia_semana, created_by)
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
                return cursor.fetchall()
        finally:
            connection.close()

    def buscar_aula_por_id(id):
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM aulas WHERE id = %s"
                cursor.execute(sql, (id,))
                return cursor.fetchone()
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
