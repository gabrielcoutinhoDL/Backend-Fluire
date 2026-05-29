from config.database import get_connection

class UsuarioModel:

    @staticmethod
    def criar_usuario(nome, email, senha_hash):
        connection = get_connection()
    
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s) RETURNING id",
                    (nome, email, senha_hash)
                )
                usuario_id = cursor.fetchone()[0]
                connection.commit()
                return usuario_id

        finally:
            connection.close()


    @staticmethod
    def buscar_usuario_nome(nome):
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, nome, email, senha, tipo_usuario FROM usuarios WHERE nome = %s",
                    (nome,)
                )
                usuario = cursor.fetchone()
                if usuario:
                    return {
                        "id": usuario[0],
                        "nome": usuario[1],
                        "email": usuario[2],
                        "senha_hash": usuario[3],
                        "tipo_usuario": usuario[4]
                    }                   
                return None

        finally:
            connection.close()
            
    @staticmethod
    def atualizar_usuario(id, nome, email, senha_hash):
        connection = get_connection()
    
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE usuarios SET nome = %s, email = %s, senha = %s WHERE id = %s",
                    (nome, email, senha_hash, id)
                )
                connection.commit()
                return cursor.rowcount > 0

        finally:
            connection.close()
    
    @staticmethod
    def deletar_usuario(id):
        connection = get_connection()
    
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM usuarios WHERE id = %s",
                    (id,)
                )
                connection.commit()
                return cursor.rowcount > 0

        finally:
            connection.close()


    @staticmethod
    def buscar_usuario_email(email):
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, nome, email, senha, tipo_usuario FROM usuarios WHERE email = %s",
                    (email,)
                )
                usuario = cursor.fetchone()
                if usuario:
                    return {
                        "id": usuario[0],
                        "nome": usuario[1],
                        "email": usuario[2],
                    }                   
                return None

        finally:
            connection.close()