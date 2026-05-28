from config.database import get_connection


class AulaAlunosModel:
    
    def associar_aluno_a_aula(aula_id, aluno_id):
        connection = get_connection()

        try:
            with connection.cursor() as cursor:

                # valida se aula existe
                cursor.execute("SELECT id FROM aulas WHERE id = %s", (aula_id,))
                if not cursor.fetchone():
                    raise Exception("Aula não encontrada")

                # valida se aluno existe
                cursor.execute("SELECT id FROM alunos WHERE id = %s", (aluno_id,))
                if not cursor.fetchone():
                    raise Exception("Aluno não encontrado")

                sql = """
                    INSERT INTO aula_alunos 
                    (aula_id, aluno_id)
                    VALUES (%s, %s)
                """

                cursor.execute(sql, (aula_id, aluno_id))
                connection.commit()

        except Exception as e:
            if "Duplicate entry" in str(e):
                raise Exception("Aluno já está nessa aula")
            connection.rollback()
            raise e

        finally:
            connection.close()
            
    def buscar_aulas_por_aluno_id(aluno_id):
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                sql = """
                    SELECT a.id, a.nome, a.usuario_id, a.horario_inicio, a.horario_fim, a.frequencia, a.dia_semana
                    FROM aulas a
                    JOIN aula_alunos aa ON a.id = aa.aula_id
                    WHERE aa.aluno_id = %s
                """
                cursor.execute(sql, (aluno_id,))
                aulas = cursor.fetchall()
                return aulas

        except Exception as e:
            raise e

        finally:
            connection.close()
            
    def remover_aluno_da_aula(aula_id, aluno_id):
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM aula_alunos WHERE aula_id = %s AND aluno_id = %s"
                cursor.execute(sql, (aula_id, aluno_id))
                connection.commit()
                return cursor.rowcount

        except Exception as e:
            connection.rollback()
            raise e

        finally:
            connection.close()