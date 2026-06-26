from config.database import get_connection


class AulasModel:

    def criar_aula(nome, usuario_id, horario_inicio, horario_fim, frequencia, dia_semana, usuario_logado_id=None):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO aulas (nome, usuario_id, horario_inicio, horario_fim, frequencia, dia_semana, created_by)
                    VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id
                    """,
                    (nome, usuario_id, horario_inicio, horario_fim, frequencia, dia_semana, usuario_logado_id)
                )
                aula_id = cursor.fetchone()["id"]
                connection.commit()
                return aula_id
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            connection.close()

    @staticmethod
    def buscar_todas_aulas():
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, nome, usuario_id, horario_inicio, horario_fim, frequencia, dia_semana, created_by, updated_by, created_at, updated_at FROM aulas"
                )
                return [
                    {
                        "id": aula["id"],
                        "nome": aula["nome"],
                        "usuario_id": aula["usuario_id"],
                        "horario_inicio": str(aula["horario_inicio"]),
                        "horario_fim": str(aula["horario_fim"]),
                        "frequencia": aula["frequencia"],
                        "dia_semana": aula["dia_semana"],
                        "created_by": aula.get("created_by"),
                        "updated_by": aula.get("updated_by"),
                        "created_at": str(aula["created_at"]) if aula.get("created_at") else None,
                        "updated_at": str(aula["updated_at"]) if aula.get("updated_at") else None,
                    }
                    for aula in cursor.fetchall()
                ]
        finally:
            connection.close()

    @staticmethod
    def buscar_aula_por_id(id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, nome, usuario_id, horario_inicio, horario_fim, frequencia, dia_semana, created_by, updated_by, created_at, updated_at FROM aulas WHERE id = %s",
                    (id,)
                )
                aula = cursor.fetchone()
                if not aula:
                    return None
                return {
                    "id": aula["id"],
                    "nome": aula["nome"],
                    "usuario_id": aula["usuario_id"],
                    "horario_inicio": str(aula["horario_inicio"]),
                    "horario_fim": str(aula["horario_fim"]),
                    "frequencia": aula["frequencia"],
                    "dia_semana": aula["dia_semana"],
                    "created_by": aula.get("created_by"),
                    "updated_by": aula.get("updated_by"),
                    "created_at": str(aula["created_at"]) if aula.get("created_at") else None,
                    "updated_at": str(aula["updated_at"]) if aula.get("updated_at") else None,
                }
        finally:
            connection.close()

    def atualizar_aula(id, nome, usuario_id, horario_inicio, horario_fim, frequencia, dia_semana, usuario_logado_id=None):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE aulas SET nome = %s, usuario_id = %s, horario_inicio = %s, horario_fim = %s, frequencia = %s, dia_semana = %s, updated_by = %s WHERE id = %s",
                    (nome, usuario_id, horario_inicio, horario_fim, frequencia, dia_semana, usuario_logado_id, id)
                )
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
                cursor.execute("DELETE FROM aulas WHERE id = %s", (id,))
                connection.commit()
                return cursor.rowcount
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            connection.close()
