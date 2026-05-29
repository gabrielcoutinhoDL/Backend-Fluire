from flask import request, jsonify
from flask_jwt_extended import create_access_token
from models.usuarios_model import criar_usuario, buscar_usuario_nome, atualizar_usuario, deletar_usuario
import os
import bcrypt
import jwt
from config.database import get_connection


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
        usuario_id = criar_usuario(nome, email, senha_hash)
        return jsonify({
            "mensagem": "Usuário criado com sucesso",
            "id": usuario_id
        }), 201
    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 400


       
def buscar_usuario_nome_controller(nome):
    usuario = buscar_usuario_nome(nome)

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
        sucesso = atualizar_usuario(id, nome, email, senha_hash)
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
        sucesso = deletar_usuario(id)
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
        