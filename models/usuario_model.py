from config.database import get_connection

class AuthModel:
    def buscar_usuario_email():
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                sql = "SELECT * from usuarios where %s"
                cursor.execute(sql, (email,))
                result = cursor.fetchall()
                return result
        finally:
            connection.close()