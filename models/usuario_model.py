from config.database import get_connection
import bcrypt
from flask_jwt_extended import create_access_token

class UsuarioModel:

    def criar_usuario(nome, email, senha_hash):
        
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)",
                    (nome, email, senha_hash)
                )

                connection.commit()

                usuario_id = cursor.lastrowid

                return usuario_id

        finally:
            connection.close()


    @staticmethod
    def buscar_usuario_nome(nome):
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, nome, email, senha FROM usuarios WHERE nome LIKE %s",
                    (f"%{nome}%",)
                )
                usuario = cursor.fetchone()
                
                if usuario:
                    return usuario
                return None
        finally:
            connection.close()
           
    @staticmethod        
    def buscar_todos_usuarios():
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, nome, email, senha FROM usuarios"
                )
                usuarios = cursor.fetchall()
                
                return usuarios

        finally:
            connection.close()
    
    
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
                    "SELECT id, nome, email, senha FROM usuarios WHERE email = %s",
                    (email,)
                )
                usuario = cursor.fetchone()
                if usuario:
                    return {
                        "id": usuario["id"],
                        "nome": usuario["nome"],
                        "email": usuario["email"]
                    }
                return None
        finally:
            connection.close()
    
            
    @staticmethod
    def login_usuario(email, senha):
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id, nome, email, senha
                    FROM usuarios
                    WHERE email = %s
                    """,
                    (email,)
                )

                usuario = cursor.fetchone()

                if not usuario:
                    return None

                senha_hash = usuario["senha"]

                if isinstance(senha_hash, str):
                    senha_hash = senha_hash.encode("utf-8")
                    
                senha_valida = bcrypt.checkpw(
                    senha.encode("utf-8"),
                    senha_hash
                )

                if not senha_valida:
                    return None

                return {
                    "id": usuario["id"],
                    "nome": usuario["nome"],
                    "email": usuario["email"]
                }

        finally:
            connection.close()