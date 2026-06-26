from config.database import get_connection


class AulaAlunosModel:

    @staticmethod
    def associar_aluno_a_aula(aula_id, aluno_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id FROM aulas WHERE id = %s", (aula_id,))
                if not cursor.fetchone():
                    raise Exception("Aula não encontrada")

                cursor.execute("SELECT id FROM alunos WHERE id = %s", (aluno_id,))
                if not cursor.fetchone():
                    raise Exception("Aluno não encontrado")

                cursor.execute(
                    "INSERT INTO aula_alunos (aula_id, aluno_id) VALUES (%s, %s) RETURNING id",
                    (aula_id, aluno_id)
                )
                relacionamento_id = cursor.fetchone()["id"]
                connection.commit()
                return relacionamento_id

        except Exception as e:
            connection.rollback()
            if "duplicate key value" in str(e):
                raise Exception("Aluno já está associado a esta aula")
            raise e
        finally:
            connection.close()

    @staticmethod
    def remover_aluno_da_aula(aula_id, aluno_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM aula_alunos WHERE aula_id = %s AND aluno_id = %s",
                    (aula_id, aluno_id)
                )
                connection.commit()
                return cursor.rowcount
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            connection.close()

    @staticmethod
    def listar_aula_alunos():
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT aa.id, aa.aula_id, aa.aluno_id,
                           a.nome as aula_nome, al.nome as aluno_nome, aa.created_at
                    FROM aula_alunos aa
                    INNER JOIN aulas a ON aa.aula_id = a.id
                    INNER JOIN alunos al ON aa.aluno_id = al.id
                    ORDER BY a.nome, al.nome
                """)
                return cursor.fetchall()
        finally:
            connection.close()

    @staticmethod
    def buscar_aula_aluno_por_id(id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT aa.id, aa.aula_id, aa.aluno_id,
                           a.nome as aula_nome, al.nome as aluno_nome, aa.created_at
                    FROM aula_alunos aa
                    INNER JOIN aulas a ON aa.aula_id = a.id
                    INNER JOIN alunos al ON aa.aluno_id = al.id
                    WHERE aa.id = %s
                """, (id,))
                return cursor.fetchone()
        finally:
            connection.close()

    @staticmethod
    def obter_alunos_por_aula(aula_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id FROM aulas WHERE id = %s", (aula_id,))
                if not cursor.fetchone():
                    raise Exception("Aula não encontrada")

                cursor.execute("""
                    SELECT aa.id, aa.aluno_id, al.nome, al.email, al.telefone, aa.created_at
                    FROM aula_alunos aa
                    INNER JOIN alunos al ON aa.aluno_id = al.id
                    WHERE aa.aula_id = %s
                    ORDER BY al.nome
                """, (aula_id,))
                return cursor.fetchall()
        finally:
            connection.close()

    @staticmethod
    def obter_aulas_por_aluno(aluno_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id FROM alunos WHERE id = %s", (aluno_id,))
                if not cursor.fetchone():
                    raise Exception("Aluno não encontrado")

                cursor.execute("""
                    SELECT aa.id, aa.aula_id, a.nome, a.horario_inicio, a.horario_fim,
                           a.dia_semana, a.frequencia, aa.created_at
                    FROM aula_alunos aa
                    INNER JOIN aulas a ON aa.aula_id = a.id
                    WHERE aa.aluno_id = %s
                    ORDER BY a.nome
                """, (aluno_id,))
                return cursor.fetchall()
        finally:
            connection.close()