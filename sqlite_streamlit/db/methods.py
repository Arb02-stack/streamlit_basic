import sqlite3


def db_conn():
    conn = sqlite3.connect("db/clientes.db")
    return conn


def insertData(nome, email, telefone):
    conn = db_conn()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tb_cliente(nome, email, telefone) VALUES (?,?,?)", (nome, email, telefone))

    conn.commit()
    cursor.close()


def listData():
    conn = db_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tb_cliente")
    data = cursor.fetchall()
    cursor.close()
    return data
