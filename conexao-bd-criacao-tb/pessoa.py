# - definir a entidade Pessoa, de forma que os atributos tenham os seguintes tipos e restrições:
#     cpf: integer (chave primária, não nulo)
#     nome: TEXT (não nulo).
#     nascimento: DATE (não nulo).
#     óculos: BOOLEAN (não nulo)

import sqlite3 as conector

try:
    # Abertura de conexão e aquisição de cursor
    conexao = conector.connect("conexao-bd-criacao-tb\\meu_banco.db")
    cursor = conexao.cursor()

    # Execução de um comando: SELECT... CREATE ...
    comando = '''CREATE TABLE Pessoa (
                     cpf INTEGER NOT NULL,
                     nome TEXT NOT NULL,
                     nascimento DATE NOT NULL,
                     oculos BOOLEAN NOT NULL,
                     PRIMARY KEY (cpf)
                     );'''

    cursor.execute(comando)

    # Efetivação do comando
    conexao.commit()

except conector.DatabaseError as erro:
    print("Erro de banco de dados", erro)

finally:
    # Fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()
