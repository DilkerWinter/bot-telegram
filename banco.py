import psycopg2
import keys
def conectar_banco():
    try:
        connection = psycopg2.connect(
            database=keys.database,
            user=keys.user,
            password=keys.password,
            host="localhost",
            port="5432"
        )
        print("Conectado com sucesso")
        return connection  # Return the connection object
    except (Exception, psycopg2.Error) as error:
        print("Erro ao conectar:", error)
        return None  # Return None in case of error

def listarProdutos(idTelegram):
    try:
        connection = conectar_banco()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM produto WHERE produto.id_Telegram = {idTelegram}")
            print("Consulta realizada com sucesso")
            return cursor.fetchall()
    except (Exception, psycopg2.Error) as error:
        print("Erro ao listar produtos:", error)
    finally:
        if connection is not None:
            connection.close()


def adicionarProdutos(idTelegram, nome, qnt, valor):
    try:
        # Conectar ao banco de dados
        connection = conectar_banco()  # Supondo que você tenha a função conectar_banco() implementada em outro lugar

        if connection is not None:
            cursor = connection.cursor()

            qnt = int(qnt)
            valor = float(valor)

            cursor.execute("INSERT INTO produto (nome, valor, quantidade, id_telegram) VALUES (%s, %s, %s, %s)",
                           (nome, valor, qnt, idTelegram))

            # Commit para efetivar a inserção
            connection.commit()

            print("Produto adicionado com sucesso")
    except (Exception, psycopg2.Error) as error:
        print("Erro ao adicionar produto:", error)
        print(nome, qnt, valor, idTelegram)
    finally:
        if connection is not None:
            connection.close()

def removerProduto(idTelegram, idProduto):
        connection = conectar_banco()
        if connection is not None:
            cursor = connection.cursor()
            idProduto = int(idProduto)

            cursor.execute(f"DELETE FROM produto WHERE id_Telegram = %s AND produto.id = %s", (idTelegram, idProduto))
            connection.commit()
            print("Produto removido com sucesso")
            return "Produto removido com sucesso"
