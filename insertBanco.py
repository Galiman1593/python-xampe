import mysql.connector
try:
    conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'escola'
    )

    cursor = conexao.cursor()

    nome = input("informe o nome: ")
    nota1 = float(input("informe nota 1: "))
    nota2 = float(input("informe nota 2: "))

    sql = "insert into alunos (nome, nota1, nota2) values(%s, %s, %s)"

    info = (nome, nota1, nota2)
    cursor.execute(sql, info)
    conexao.commit()

    cursor.close()
    conexao.close()
except:
    print("erro ao cadastrar")    