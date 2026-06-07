from flask import request, jsonify
from flask_jwt_extended import jwt_required

from models.aula_alunos_model import AulaAlunosModel


@jwt_required()
def associar_aluno_a_aula_controller():

    dados = request.json

    aula_id = dados.get("aula_id")
    aluno_id = dados.get("aluno_id")

    if not aula_id:
        return jsonify({
            "erro": "Aula obrigatória"
        }), 400

    if not aluno_id:
        return jsonify({
            "erro": "Aluno obrigatório"
        }), 400

    try:
        relacionamento_id = AulaAlunosModel.associar_aluno_a_aula(
            aula_id,
            aluno_id
        )

        return jsonify({
            "mensagem": "Aluno associado à aula com sucesso",
            "id": relacionamento_id
        }), 201

    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 400


@jwt_required()
def remover_aluno_da_aula_controller():

    dados = request.json

    aula_id = dados.get("aula_id")
    aluno_id = dados.get("aluno_id")

    if not aula_id:
        return jsonify({
            "erro": "Aula obrigatória"
        }), 400

    if not aluno_id:
        return jsonify({
            "erro": "Aluno obrigatório"
        }), 400

    try:
        linhas_afetadas = AulaAlunosModel.remover_aluno_da_aula(
            aula_id,
            aluno_id
        )

        if linhas_afetadas == 0:
            return jsonify({
                "erro": "Relacionamento não encontrado"
            }), 404

        return jsonify({
            "mensagem": "Aluno removido da aula com sucesso"
        }), 200

    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 400


@jwt_required()
def listar_aula_alunos_controller():
    try:
        aula_alunos = AulaAlunosModel.listar_aula_alunos()

        if not aula_alunos:
            return jsonify({
                "mensagem": "Nenhuma associação encontrada",
                "dados": []
            }), 200

        resultado = [
            {
                "id": aa["id"],
                "aula_id": aa["aula_id"],
                "aluno_id": aa["aluno_id"],
                "aula_nome": aa["aula_nome"],
                "aluno_nome": aa["aluno_nome"],
                "criado_em": aa["created_at"]
            }
            for aa in aula_alunos
        ]

        return jsonify({
            "mensagem": "Associações listadas com sucesso",
            "total": len(resultado),
            "dados": resultado
        }), 200

    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 400


@jwt_required()
def buscar_aula_aluno_por_id_controller(id):
    try:
        aula_aluno = AulaAlunosModel.buscar_aula_aluno_por_id(id)

        if not aula_aluno:
            return jsonify({
                "erro": "Associação não encontrada"
            }), 404

        resultado = {
            "id": aula_aluno["id"],
            "aula_id": aula_aluno["aula_id"],
            "aluno_id": aula_aluno["aluno_id"],
            "aula_nome": aula_aluno["aula_nome"],
            "aluno_nome": aula_aluno["aluno_nome"],
            "criado_em": aula_aluno["created_at"]
        }

        return jsonify({
            "mensagem": "Associação encontrada com sucesso",
            "dados": resultado
        }), 200

    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 400


@jwt_required()
def obter_alunos_por_aula_controller(aula_id):
    try:
        alunos = AulaAlunosModel.obter_alunos_por_aula(aula_id)

        if not alunos:
            return jsonify({
                "mensagem": "Nenhum aluno associado a esta aula",
                "dados": []
            }), 200

        resultado = [
            {
                "id": aluno["id"],
                "aluno_id": aluno["aluno_id"],
                "nome": aluno["nome"],
                "email": aluno["email"],
                "telefone": aluno["telefone"],
                "associado_em": aluno["created_at"]
            }
            for aluno in alunos
        ]

        return jsonify({
            "mensagem": "Alunos da aula listados com sucesso",
            "total": len(resultado),
            "dados": resultado
        }), 200

    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 400


@jwt_required()
def obter_aulas_por_aluno_controller(aluno_id):
    try:
        aulas = AulaAlunosModel.obter_aulas_por_aluno(aluno_id)

        if not aulas:
            return jsonify({
                "mensagem": "Este aluno não está associado a nenhuma aula",
                "dados": []
            }), 200

        resultado = [
            {
                "id": aula["id"],
                "aula_id": aula["aula_id"],
                "nome": aula["nome"],
                "horario_inicio": aula["horario_inicio"],
                "horario_fim": aula["horario_fim"],
                "dia_semana": aula["dia_semana"],
                "frequencia": aula["frequencia"],
                "associado_em": aula["created_at"]
            }
            for aula in aulas
        ]

        return jsonify({
            "mensagem": "Aulas do aluno listadas com sucesso",
            "total": len(resultado),
            "dados": resultado
        }), 200

    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 400