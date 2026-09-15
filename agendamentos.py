import mysql.connector
from banco import conectar

from models import Agendamento

def listar_agendamentos():

    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM agendamentos")
        return [Agendamento.reverte_tupla(linha) for linha in cursor.fetchall()]

    except mysql.connector.Error as erro:
        print(f"Erro ao listar {erro}")

    finally:
        if conexao is conexao.is_connected():
            conexao.close()




def buscar_agendamento(id):
    conexao = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM agendamentos WHERE id = %s",(id,))
        agendamento = cursor.fetchone()
        if not agendamento:
            print(f"Nenhum agendamento com o id {id} encontrado!")
            return None

        return Agendamento.reverte_tupla(agendamento)

    except mysql.connector.Error as erro:
        print(f"Erro ao buscar {erro}")

    finally:
        if conexao is conexao.is_connected():
            conexao.close()



def listar_por_status(status):
    conexao = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM agendamentos WHERE status_agendamento = %s",(status,))

        return [Agendamento.reverte_tupla(linha) for linha in cursor.fetchall()]

    except mysql.connector.Error as erro:
        print(f"Erro ao buscar {erro}")

    finally:
        if conexao is conexao.is_connected():
            conexao.close()
