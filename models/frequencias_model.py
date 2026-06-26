from config.database import get_connection


# presente é BOOLEAN no PostgreSQL: True = presente, False = ausente

def buscar_todas_frequencias():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM frequencias")
            return cursor.fetchall()
    finally:
        connection.close()


def buscar_frequencias_por_aula_model(aula_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM frequencias WHERE aula_id = %s", (aula_id,))
            return cursor.fetchall()
    finally:
        connection.close()


def buscar_frequencias_por_id_model(id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM frequencias WHERE id = %s", (id,))
            return cursor.fetchall()
    finally:
        connection.close()


def verificar_frequencias_existente(aula_id, aluno_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM frequencias WHERE aula_id = %s AND aluno_id = %s",
                (aula_id, aluno_id)
            )
            return cursor.fetchone()
    finally:
        connection.close()


def inserir_frequencias_model(aula_id, aluno_id, presente):
    from datetime import date
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO frequencias (aula_id, aluno_id, presente, data_presenca) VALUES (%s, %s, %s, %s)",
                (aula_id, aluno_id, bool(presente), date.today())
            )
            connection.commit()
    finally:
        connection.close()


def atualizar_frequencias(id, presente):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE frequencias SET presente = %s WHERE id = %s",
                (bool(presente), id)
            )
            connection.commit()
    finally:
        connection.close()


def deletar_frequencias_model(id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM frequencias WHERE id = %s", (id,))
            connection.commit()
            return cursor.rowcount
    finally:
        connection.close()