# - adicionar mais um atributo à entidade Veículo
# - atributo se chama motor e corresponde à motorização do carro: 1.0, 1.4, 2.0 etc
# - Esse atributo deverá conter pontos flutuantes e, por isso, vamos defini-lo como do tipo REAL.

# - Para alterar a tabela Veículo e adicionar a coluna motor, utilizamos o seguinte comando SQL.

# ALTER TABLE Veiculo
# ADD motor REAL;

import sqlite3 as conector

# Abertura de conexão e aquisição de cursor
conexao = conector.connect("conexao-bd-criacao-tb\\meu_banco.db")
cursor = conexao.cursor()

# Execução de um comando: SELECT... CREATE ...
comando = '''ALTER TABLE Veiculo
                ADD motor REAL;'''

cursor.execute(comando)

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()