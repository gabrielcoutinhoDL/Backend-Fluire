from flask import request, jsonify, current_app
from flask_jwt_extended import create_access_token
from models.usuario_model import UsuarioModel
import bcrypt
from flask_mail import Message, Mail
import random
from config.database import get_connection

# Validado no postman
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

    # Verificar se email já existe
    usuario_existente = UsuarioModel.buscar_usuario_email(email)
    if usuario_existente:
        return jsonify({
            "erro": "Email já cadastrado"
        }), 400

    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

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

# Validado no postman
def buscar_usuario_nome_controller(nome):
    try:
        usuario = UsuarioModel.buscar_usuario_nome(nome)

        if not usuario:
            return jsonify({
                "erro": "Usuário não encontrado"
            }), 404

        return jsonify(usuario), 200

    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 500

# Validado no postman
def buscar_todos_usuarios_controller():
    usuario = UsuarioModel.buscar_todos_usuarios()

    return jsonify(usuario), 200


# Validado no postman
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

# Validado no postman
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
        
# Validado no postman
def login_usuario_controller():
    try:
        dados = request.json

        email = dados.get("email")
        senha = dados.get("senha")

        if not email:
            return jsonify({
                "erro": "Email é obrigatório"
            }), 400

        if not senha:
            return jsonify({
                "erro": "Senha é obrigatória"
            }), 400

        usuario = UsuarioModel.login_usuario(email, senha)

        if not usuario:
            return jsonify({
                "erro": "Email ou senha inválidos"
            }), 401

        token = create_access_token(identity=str(usuario["id"])) 

        return jsonify({
            "mensagem": "Login realizado com sucesso",
            "token": token,
            "usuario": {
                "id": usuario["id"],
                "nome": usuario["nome"],
                "email": usuario["email"]
            }
        }), 200

    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 500


#recuperar senha
def recuperar_senha_controller():
    try:
        dados = request.json
        email = dados.get("email")
        
        if not email:
            return jsonify({
                "erro": "Email é obrigatório"
            }), 400

        usuario = UsuarioModel.buscar_usuario_email(email)
        
        if not usuario:
            return jsonify({
                "erro": "Email não encontrado"
            }), 404

        # Gerar codigo de recuperação
        codigo_recuperacao = str(random.randint(100000, 999999))
        
        # Enviar email com codigo de recuperação
        msg = Message("Código de Recuperação de Senha", sender="ademirjose12340@gmail.com", recipients=[email])
           
        msg.body = f"Olá {usuario['nome']},\n\nSeu código de recuperação de senha é: {codigo_recuperacao}\n\nSe você não solicitou a recuperação de senha, ignore este email."

        current_app.extensions['mail'].send(msg)

        return jsonify({
            "mensagem": "Código de recuperação enviado para o email"
        }), 200
        
    except Exception as e:
        import traceback

        traceback.print_exc()

        return jsonify({
            "erro": str(e),
            "tipo": type(e).__name__
        }), 500