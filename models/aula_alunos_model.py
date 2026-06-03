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