from config.database import get_connection

# Model para gerenciar as frequências dos alunos nas aulas
# Toda a frequencia usa o TINYINT para armazenar se o aluno está presente ou ausente, onde 1 representa presente e 0 representa ausente

def buscar_todas_frequencias():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM frequencias")
        frequencias = cursor.fetchall()

        cursor.close()
        connection.close()

        return frequencias
    except Exception as e:
        raise Exception(f"Erro ao buscar todas as frequências: {str(e)}")
    
def buscar_frequencias_por_aula(aula_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM frequencias WHERE aula_id = %s", (aula_id,))
        frequencias = cursor.fetchall()

        cursor.close()
        connection.close()

        return frequencias
    except Exception as e:
        raise Exception(f"Erro ao buscar frequências por aula: {str(e)}")
    
def verificar_frequencia_existente(aula_id, aluno_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM frequencias WHERE aula_id = %s AND aluno_id = %s", (aula_id, aluno_id))
        frequencia = cursor.fetchone()

        cursor.close()
        connection.close()

        return frequencia
    except Exception as e:
        raise Exception(f"Erro ao verificar frequência existente: {str(e)}")
    
def inserir_frequencia_model(aula_id, aluno_id, presente):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO frequencias (aula_id, aluno_id, presente) VALUES (%s, %s, %s)",
            (aula_id, aluno_id, presente)
        )
        connection.commit()

        cursor.close()
        connection.close()
    except Exception as e:
        raise Exception(f"Erro ao inserir frequência: {str(e)}")
    
def atualizar_frequencia(id, presente):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE frequencias SET presente = %s WHERE id = %s",
            (presente, id)
        )
        connection.commit()

        cursor.close()
        connection.close()
    except Exception as e:
        raise Exception(f"Erro ao atualizar frequência: {str(e)}")
    
def deletar_frequencia(id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("DELETE FROM frequencias WHERE id = %s", (id,))
        connection.commit()

        cursor.close()
        connection.close()
    except Exception as e:
        raise Exception(f"Erro ao deletar frequência: {str(e)}")