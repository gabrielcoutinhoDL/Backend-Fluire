from config.database import get_connection
import bcrypt
from datetime import datetime, timedelta


class UsuarioModel:

    def criar_usuario(nome, email, senha_hash):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s) RETURNING id",
                    (nome, email, senha_hash)
                )
                usuario_id = cursor.fetchone()["id"]
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
                    "SELECT id, nome, email, senha FROM usuarios WHERE nome LIKE %s",
                    (f"%{nome}%",)
                )
                return cursor.fetchone()
        finally:
            connection.close()

    @staticmethod
    def buscar_todos_usuarios():
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, nome, email, senha FROM usuarios")
                return cursor.fetchall()
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
                cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
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
                if not usuario:
                    return None
                return {"id": usuario["id"], "nome": usuario["nome"], "email": usuario["email"]}
        finally:
            connection.close()

    @staticmethod
    def login_usuario(email, senha):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, nome, email, senha FROM usuarios WHERE email = %s",
                    (email,)
                )
                usuario = cursor.fetchone()
                if not usuario:
                    return None

                senha_hash = usuario["senha"]
                if isinstance(senha_hash, str):
                    senha_hash = senha_hash.encode("utf-8")

                if not bcrypt.checkpw(senha.encode("utf-8"), senha_hash):
                    return None

                return {"id": usuario["id"], "nome": usuario["nome"], "email": usuario["email"]}
        finally:
            connection.close()

    @staticmethod
    def salvar_codigo_recuperacao(email, codigo):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                expiracao = datetime.now() + timedelta(minutes=15)
                cursor.execute(
                    "UPDATE usuarios SET codigo_recuperacao = %s, codigo_expiracao = %s WHERE email = %s",
                    (codigo, expiracao, email)
                )
                connection.commit()
                return cursor.rowcount > 0
        finally:
            connection.close()

    @staticmethod
    def validar_codigo_recuperacao(email, codigo):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, nome, email, codigo_recuperacao, codigo_expiracao FROM usuarios WHERE email = %s",
                    (email,)
                )
                usuario = cursor.fetchone()
                if not usuario:
                    return None

                codigo_salvo = usuario.get("codigo_recuperacao")
                expiracao = usuario.get("codigo_expiracao")

                if not codigo_salvo or not expiracao:
                    return None
                if codigo_salvo != codigo:
                    return None
                if datetime.now() > expiracao:
                    return None

                return {"id": usuario["id"], "nome": usuario["nome"], "email": usuario["email"]}
        finally:
            connection.close()

    @staticmethod
    def alterar_senha(usuario_id, nova_senha_hash):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE usuarios SET senha = %s, codigo_recuperacao = NULL, codigo_expiracao = NULL WHERE id = %s",
                    (nova_senha_hash, usuario_id)
                )
                connection.commit()
                return cursor.rowcount > 0
        finally:
            connection.close()