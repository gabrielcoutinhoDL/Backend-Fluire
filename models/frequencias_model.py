from config.database import get_connection


def buscar_todas_frequencias():
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            sql = " SELECT f.id, f.aula_id, f.aluno_id, a.nome AS aluno_nome, f.data_presenca, f.presente FROM frequencias f INNER JOIN alunos a ON a.id = f.aluno_id ORDER BY f.data_presenca DESC, a.nome ASC "
            
            cursor.execute(sql)
            return cursor.fetchall()

    finally:
        connection.close()


def buscar_frequencias_por_aula(aula_id):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            sql = "SELECT f.id, f.aula_id, f.aluno_id, a.nome AS aluno_nome, f.data_presenca, f.presente FROM frequencias f INNER JOIN alunos a ON a.id = f.aluno_id WHERE f.aula_id = %s ORDER BY a.nome ASC"
            
            cursor.execute(sql, (aula_id,))
            return cursor.fetchall()
    finally:
        connection.close()


def verificar_frequencia_existente(aula_id, aluno_id, data_presenca):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            sql = """
                SELECT id
                FROM frequencias
                WHERE aula_id = %s AND aluno_id = %s AND data_presenca = %s
            """
            cursor.execute(sql, (aula_id, aluno_id, data_presenca))
            return cursor.fetchone()
    finally:
        connection.close()


def inserir_frequencia(aula_id, aluno_id, presente, data_presenca):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            sql = """
                INSERT INTO frequencias (aula_id, aluno_id, presente, data_presenca)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (aula_id, aluno_id, presente, data_presenca))
            connection.commit()
    finally:
        connection.close()


def atualizar_frequencia(id, presente):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            sql = "UPDATE frequencias SET presente = %s WHERE id = %s"
            cursor.execute(sql, (presente, id))
            connection.commit()
    finally:
        connection.close()


def deletar_frequencia(id):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM frequencias WHERE id = %s"
            cursor.execute(sql, (id,))
            connection.commit()
    finally:
        connection.close()
