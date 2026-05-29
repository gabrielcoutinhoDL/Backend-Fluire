from flask import request, jsonify, current_app
from flask_jwt_extended import create_access_token
from models.usuario_model import UsuarioModel
import os
import bcrypt
import jwt
from config.database import get_connection
from flask_mail import Message
import random


def criar_usuario_controller():
    dados = request.json

    nome = dados.get("nome")
    email = dados.get("email")
    senha = dados.get("senha")

    
    # validações
    if not nome:
        return jsonify({
            "erro": "Nome obrigatório"
        }), 400

    if not email:
        return jsonify({
            "erro": "Email obrigatório"
        }), 400

    if not senha:
        return jsonify({
            "erro": "Senha obrigatória"
        }), 400

    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

    try:
        usuario_id = UsuarioModel.criar_usuario(nome, email, senha_hash)
        return jsonify({
            "mensagem": "Usuário criado com sucesso",
            "id": usuario_id
        }), 201
    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 400


       
def buscar_usuario_nome_controller(nome):
    usuario = UsuarioModel.buscar_usuario_nome(nome)

    if not usuario:
        return jsonify({
            "erro": "Usuário não encontrado"
        }), 404

    return jsonify(usuario), 200

def atualizar_usuario_controller(id):
    dados = request.json

    nome = dados.get("nome")
    email = dados.get("email")
    senha = dados.get("senha")

    if not nome:
        return jsonify({
            "erro": "Nome obrigatório"
        }), 400

    if not email:
        return jsonify({
            "erro": "Email obrigatório"
        }), 400

    if not senha:
        return jsonify({
            "erro": "Senha obrigatória"
        }), 400

    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

    try:
        sucesso = UsuarioModel.atualizar_usuario(id, nome, email, senha_hash)
        if sucesso:
            return jsonify({
                "mensagem": "Usuário atualizado com sucesso"
            }), 200
        else:
            return jsonify({
                "erro": "Usuário não encontrado"
            }), 404
    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 400

def deletar_usuario_controller(id):
    try:
        sucesso = UsuarioModel.deletar_usuario(id)
        if sucesso:
            return jsonify({
                "mensagem": "Usuário deletado com sucesso"
            }), 200
        else:
            return jsonify({
                "erro": "Usuário não encontrado"
            }), 404
    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 400
        
        
def login_usuario_controller():
    dados = request.json

    email = dados.get("email")
    senha = dados.get("senha")

    connection = get_connection()
    cursor = connection.cursor()
    
    sql = """SELECT * FROM usuarios WHERE email = %s"""
    try:
        cursor.execute(sql, (email,))
        usuario = cursor.fetchone()

        if usuario:
            if bcrypt.checkpw(senha.encode('utf-8'), usuario['senha'].encode('utf-8')):
                token = create_access_token(identity=usuario['id'])
                
                response = {"mensagem": "Login bem-sucedido", "usuario": {
                    "id": usuario['id'],
                    "nome": usuario['nome'],
                    "email": usuario['email'] 
                }, "token": token}
                
                return jsonify(response), 200
            else:
                return jsonify({"erro": "Senha incorreta"}), 401
            
    except Exception as e:
        return jsonify({"message": "Erro ao processar login", "erro": str(e)}), 401
    finally:
        connection.close()
    
    #recuperar senha

def recuperar_senha_controller():
    dados = request.json
    email = dados.get("email")

    if not email:
        return jsonify({
            "erro": "Email é obrigatório"
        }), 400

    # Verificar se o email existe no banco
    usuario = UsuarioModel.buscar_usuario_email(email)

    if not usuario:
        return jsonify({
            "erro": "Email não encontrado"
        }), 404

    # Gerar código aleatório de 6 dígitos
    codigo = random.randint(100000, 999999)

    try:
        msg = Message(
            "Recuperacao de senha",
            recipients=[email]
        )

        msg.body = f"O seu código de recuperação é: {codigo}"

        current_app.extensions['mail'].send(msg)

        return jsonify({
            "mensagem": "Codigo enviado com sucesso"
        }), 200

    except Exception as e:
        return jsonify({
            "erro": "Erro ao enviar email",
            "detalhes": str(e)
        }), 500
