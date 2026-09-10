import mysql.connector
from mysql.connector import Error

HOST = "localhost"
USER = "root"
PASSWORD = "root"
DATABASE = "barbearia"

def conectar():
    try:
        conexao = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )
        if conexao.is_connected():
            return conexao

    except Error as erro:
        print(f"Erro ao conectar: {erro}")
        return None

if __name__ == "__main__":
    conexao = conectar()
    print("Conectada com sucesso.")