# - definir a entidade Marca, de forma que os atributos tenham os seguintes tipos e restrições:
#   Id: INTEGER (chave primária, não nulo).
#   nome: TEXT (não nulo).
#   CHARACTER (não nulo, tamanho 2).

import sqlite3 as conector

# Abertura de conexão e aquisição de cursor
conexao = conector.connect("conexao-bd-criacao-tb\\meu_banco.db")
cursor = conexao.cursor()

# Execução de um comando: SELECT... CREATE ...
comando = '''CREATE TABLE Marca (
                id INTEGER NOT NULL,
                nome TEXT NOT NULL,
                sigla CHARACTER(2) NOT NULL,
                PRIMARY KEY (id)
                );'''

cursor.execute(comando)

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()
