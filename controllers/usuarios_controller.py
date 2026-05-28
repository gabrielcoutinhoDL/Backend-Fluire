from flask import request, jsonify
from models.usuario_model import *
import bcrypt

def controller_usuario():
    dados = request.json

    email = dados.get("email")
    senha = dados.get("senha")

    #verifações dos emails e senhas
    if not email or not senha :
        return jsonify({
            "erro": "preencha todos os campos por favor"
        }), 401
    
    usuario = AuthModel.buscar_usuario_email(email)

    #VEREFICANDO SE USUARIO EXISTE (se tentar 
    # fazer tudo junto ele poca)

    if not usuario:
        return jsonify({
            "erro": "usuario não encontrado"
        }), 404

    #Compara uma senha fornecida como hash armazenado
    # no banco de dados, ai ele diz se é true ou false
    senha_correta = bcrypt.checkpw(
        senha.encode("utf-8"),
        usuario["senha_hash"].encode("utf-8")
    )

    if not senha_correta:
        return jsonify({
            "erro": "senha invalida"
        }),422

    return jsonify({
        "mensagem": "Login realizado com sucesso",
        "usuario": {
            "id": usuario["id"],
            "nome": usuario["nome"],
            "email": usuario["email"],
            "tipo_usuario": usuario["tipo_usuario"]
        }
    }), 200